# -*- coding: utf-8 -*-
from openprocurement.api.utils.manager_discovery import ManagerDiscovery
from openprocurement.contracting.core.constants import DEFAULT_CONTRACT_TYPE


class ContractManagerDiscovery(ManagerDiscovery):

    _contract_type_field_name = 'contractType'

    def __init__(self, manager_registry):
        self._manager_registry = manager_registry

    def discover(self, data):
        import ipdb; ipdb.set_trace()
        contract_type_name = data.get(self._contract_type_field_name, DEFAULT_CONTRACT_TYPE)

        manager = self._manager_registry.get_manager(contract_type_name)

        if not manager:
            # TODO: raise proper exception
            # request.errors.add('body', 'data', 'contractType Not implemented')
            # request.errors.status = 415
            # raise error_handler(request)
            pass

        return manager
