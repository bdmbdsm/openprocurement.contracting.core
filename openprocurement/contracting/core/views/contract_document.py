# -*- coding: utf-8 -*-
from openprocurement.api.utils import (
    APIResource,
    json_view,
    get_file,
)
from openprocurement.contracting.core.utils import (
    contractingresource,
)
from openprocurement.contracting.core.constants import (
    ENDPOINTS,
)
from openprocurement.api.validation import validate_data_to_event
from openprocurement.contracting.core.manager_discovery import ContractManagerDiscovery
from openprocurement.api.utils.documents import DocumentUploadReader
from openprocurement.api.utils.error_management import handle_errors_on_view


@contractingresource(
    name="Contract document",
    path=ENDPOINTS['documents'],
    collection_path=ENDPOINTS['documents_collection'])
class CeasefireContractDocumentResource(APIResource):

    @json_view(
        content_type="application/json",
        validators=(validate_data_to_event,),
        permission='edit_contract')
    @handle_errors_on_view
    def collection_post(self):
        event = self.request.event
        md = ContractManagerDiscovery(self.request.registry.manager_registry)
        manager = md.discover(event.ctx.high).document_manager()
        upl_rdr = DocumentUploadReader()
        event.ctx.cache.document = upl_rdr.read(self.request)
        self.request.response.status = 201
        return manager.create_document(event)

    @json_view(content_type="application/json", permission='view_listing')
    def get(self):
        if self.request.params.get('download'):
            return get_file(self.request)
        document = self.request.validated['document']
        return {'data': document.serialize("view")}

    @json_view(
            content_type="application/json",
            validators=(validate_data_to_event,),
            permission='edit_contract')
    @handle_errors_on_view
    def patch(self):
        event = self.request.event
        md = ContractManagerDiscovery(self.request.registry.manager_registry)
        manager = md.discover(event.ctx.high).document_manager()
        return manager.change_document(event)

    @json_view(
        content_type="application/json",
        validators=(validate_data_to_event,),
        permission='edit_contract')
    @handle_errors_on_view
    def put(self):
        event = self.request.event
        md = ContractManagerDiscovery(self.request.registry.manager_registry)
        manager = md.discover(event.ctx.high).document_manager()
        upl_rdr = DocumentUploadReader()
        event.ctx.cache.document = upl_rdr.read(self.request)
        return manager.put_document(event)
