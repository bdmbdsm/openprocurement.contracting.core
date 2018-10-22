# -*- coding: utf-8 -*-
from openprocurement.api.adapters import ContentConfigurator
from openprocurement.api.managers import Manager  # noqa: forwarded import


class ContractConfigurator(ContentConfigurator):
    """ Contract configuration adapter """

    name = "Contract Configurator"
    model = None
