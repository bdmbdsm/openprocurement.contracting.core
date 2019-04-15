# -*- coding: utf-8 -*-
from logging import getLogger
from pkg_resources import get_distribution
from pyramid.interfaces import IRequest

from openprocurement.api.interfaces import IContentConfigurator
from openprocurement.api.utils.plugins import (
    get_plugin_aliases,
    get_evenly_plugins,
)

from openprocurement.contracting.core.adapters import ContractConfigurator
from openprocurement.contracting.core.design import add_design
from openprocurement.contracting.core.models import IContract
from openprocurement.contracting.core.utils import (
    isContract,
    register_contract_contractType,
    contract_from_data,
    extract_contract,
)


PKG = get_distribution(__package__)

LOGGER = getLogger(PKG.project_name)


def includeme(config, plugin_map):
    LOGGER.info('Init contracting.core plugin.')
    # contractType plugins support
    add_design()
    config.add_request_method(extract_contract, 'contract', reify=True)
    config.add_request_method(contract_from_data)
    config.scan("openprocurement.contracting.core.views")
    config.registry.contract_contractTypes = {}
    config.registry.contract_type_configurator = {}
    config.add_route_predicate('internal_type', isContract)
    config.add_directive('add_contract_contractType',
                         register_contract_contractType)
    config.scan("openprocurement.contracting.core.views")
    config.registry.registerAdapter(ContractConfigurator, (IContract, IRequest),
                                    IContentConfigurator)
    # Aliases information
    LOGGER.info('Start aliases')
    get_plugin_aliases(plugin_map.get('plugins', {}))
    LOGGER.info('End aliases')

    # add accreditation
    config.registry.accreditation['contract'] = {}

    # search for plugins
    get_evenly_plugins(config, plugin_map['plugins'], 'openprocurement.contracting.core.plugins')
