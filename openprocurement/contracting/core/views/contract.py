# -*- coding: utf-8 -*-
from openprocurement.api.utils import (
    APIResourceListing,
    json_view,
)
from openprocurement.contracting.core.utils import (
    contractingresource,
    contract_serialize,
)
from openprocurement.contracting.core.design import (
    FIELDS,
    contracts_by_dateModified_view,
    contracts_real_by_dateModified_view,
    contracts_test_by_dateModified_view,
    contracts_by_local_seq_view,
    contracts_real_by_local_seq_view,
    contracts_test_by_local_seq_view,
)
from openprocurement.api.utils.validation import validate_data_to_event
from openprocurement.api.utils.error_management import handle_errors_on_view
from openprocurement.contracting.core.manager_discovery import ContractManagerDiscovery

VIEW_MAP = {
    u'': contracts_real_by_dateModified_view,
    u'test': contracts_test_by_dateModified_view,
    u'_all_': contracts_by_dateModified_view,
}

CHANGES_VIEW_MAP = {
    u'': contracts_real_by_local_seq_view,
    u'test': contracts_test_by_local_seq_view,
    u'_all_': contracts_by_local_seq_view,
}

FEED = {
    u'dateModified': VIEW_MAP,
    u'changes': CHANGES_VIEW_MAP,
}


@contractingresource(name='Contracts',
                     path='/contracts',
                     description="Contracts")
class ContractsResource(APIResourceListing):
    """ Contract resource used only for contract listing """

    def __init__(self, request, context):
        super(ContractsResource, self).__init__(request, context)
        # params for listing
        self.VIEW_MAP = VIEW_MAP
        self.CHANGES_VIEW_MAP = CHANGES_VIEW_MAP
        self.FEED = FEED
        self.FIELDS = FIELDS
        self.serialize_func = contract_serialize
        self.object_name_for_listing = 'Contracts'
        self.log_message_id = 'contract_list_custom'

    @json_view(content_type="application/json", permission='create_contract',
               validators=(validate_data_to_event,))
    @handle_errors_on_view
    def post(self):
        event = self.request.event
        md = ContractManagerDiscovery(self.request.registry.manager_registry)
        manager = md.discover(event.data)()
        self.request.response.status = 201
        return manager.create_contract(event)
