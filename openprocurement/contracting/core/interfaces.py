# -*- coding: utf-8 -*-
from openprocurement.api.interfaces import (
    IResourceManager,
)


class IContractManager(IResourceManager):

    def create_contract(self, request, **kwargs):
        raise NotImplementedError

    def change_contract(self, request, **kwargs):
        raise NotImplementedError


class IMilestoneManager(IResourceManager):

    def create_milestones(self, request, **kwargs):
        raise NotImplementedError

    def change_milestone(self, request, **kwargs):
        raise NotImplementedError


class IDocumentManager(IResourceManager):

    def create_document(self, request, **kwargs):
        raise NotImplementedError

    def change_document(self, request, **kwargs):
        raise NotImplementedError
