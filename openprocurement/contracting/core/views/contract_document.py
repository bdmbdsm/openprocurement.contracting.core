# -*- coding: utf-8 -*-
from openprocurement.api.utils import (
    APIResource,
    json_view,
)
from openprocurement.contracting.core.utils import (
    contractingresource,
)
from openprocurement.contracting.core.constants import (
    ENDPOINTS,
)


@contractingresource(
    name="Contract document",
    path=ENDPOINTS['documents'],
    collection_path=ENDPOINTS['documents_collection'])
class CeasefireContractDocumentResource(APIResource):

    @json_view()
    def collection_post(self):
        pass
