# -*- coding: utf-8 -*-
from openprocurement.api.traversal import get_item

from pyramid.security import (
    ALL_PERMISSIONS,
    Allow,
    Everyone,
)


class Root(object):
    __name__ = None
    __parent__ = None
    __acl__ = [
        (Allow, Everyone, 'view_listing'),
        (Allow, Everyone, 'view_contract'),
        (Allow, 'g:contracting', 'create_contract'),
        (Allow, 'g:caravan', 'view_contract'),
        (Allow, 'g:caravan', 'edit_contract'),
        (Allow, 'g:brokers', 'create_contract'),
        (Allow, 'g:convoy', 'create_contract'),
        (Allow, 'g:Administrator', 'edit_contract'),
    ]

    def __init__(self, request):
        self.request = request
        self.db = request.registry.db


def factory(request):
    request.validated['contract_src'] = {}
    root = Root(request)
    if not request.matchdict or not request.matchdict.get('contract_id'):
        return root
    request.validated['contract_id'] = request.matchdict['contract_id']
    contract = request.contract
    contract.__parent__ = root
    request.validated['contract'] = request.validated['db_doc'] = contract
    if request.matchdict.get('milestone_id'):
        return get_item(contract, 'milestone', request)
    if request.method != 'GET':
        request.validated['contract_src'] = request.validated['global_ctx_plain'] = contract.serialize('plain')
    if request.matchdict.get('document_id'):
        return get_item(contract, 'document', request)
    if request.matchdict.get('change_id'):
        return get_item(contract, 'change', request)
    request.validated['id'] = request.matchdict['contract_id']
    return contract
