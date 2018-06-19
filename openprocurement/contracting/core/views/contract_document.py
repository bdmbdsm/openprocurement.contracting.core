# -*- coding: utf-8 -*-
from openprocurement.api.utils import (
    APIResource,
    json_view,
    context_unpack,
)
from openprocurement.contracting.core.utils import (
    contractingresource,
    save_contract,
)
from openprocurement.contracting.core.interfaces import (
    IDocumentManager,
)
from openprocurement.contracting.core.constants import (
    ENDPOINTS,
)
from openprocurement.contracting.core.validation import (
    validate_contract_document,
)


@contractingresource(
    name="Contract document",
    path=ENDPOINTS['documents'],
    collection_path=ENDPOINTS['documents_collection'])
class CeasefireContractDocumentResource(APIResource):

    @json_view(
        content_type="application/json",
        validators=(validate_contract_document,))
    def collection_post(self):
        document = self.request.validated['document']
        manager = self.request.registry.getAdapter(document, IDocumentManager)
        manager.create_document(self.request)
        if save_contract(self.request):
            self.LOGGER.info(
                'Created contract document. contract ID: {0} documentID: {1}'.format(
                    document.__parent__.id,
                    document.id
                ),
                extra=context_unpack(
                    self.request,
                    {'MESSAGE_ID': 'contract_document_create'},
                    {
                        'contract_id': document.__parent__.id,
                        'document_id': document.id
                    }
                )
            )
            self.request.response.status = 201
            return {
                'data': document.serialize("view"),
            }
