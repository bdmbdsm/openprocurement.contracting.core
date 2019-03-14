# -*- coding: utf-8 -*-
from pyramid.threadlocal import get_current_registry

from openprocurement.api.utils.model_discovery import ModelDiscovery
from openprocurement.contracting.core.utils import get_contract_types
from openprocurement.contracting.core.constants import DEFAULT_CONTRACT_TYPE


class ContractingModelDiscovery(ModelDiscovery):

    _contract_type_field_name = 'contractType'

    def __init__(self):
        self._registry = get_current_registry()
        self._default_contract_type = self._get_default_contract_type()

    def discover(self, data):
        contract_type_name = data.get(self._contract_type_field_name, self._default_contract_type)

        model = self._registry.contract_contractTypes.get(contract_type_name)

        if not model:
            # TODO: raise proper exception
            # request.errors.add('body', 'data', 'contractType Not implemented')
            # request.errors.status = 415
            # raise error_handler(request)
            pass

        return model

    def _get_default_contract_type(self):
        contract_types = get_contract_types(self._registry, (DEFAULT_CONTRACT_TYPE,))
        contractType = contract_types[0] if contract_types else DEFAULT_CONTRACT_TYPE

        return contractType
