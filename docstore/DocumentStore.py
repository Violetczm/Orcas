#! /usr/bin/env python


class DocumentStore(object):
    """
    Interface - This is a dictionary of document id to document content and metadata.
    """

    def get_document(self, doc_id):
        raise NotImplementedError('DocumentStores must implement get_document()')

    def set_document(self, doc_id, doc_obj):
        raise NotImplementedError('DocumentStores must implement set_document()')


class InMemoryDocumentStore(DocumentStore):
    def __init__(self, redis_client_params=None):
        self.dict = {}

    def get_document(self, doc_id):
        return self.dict.get(doc_id, None)

    def set_document(self, doc_id, doc_obj):
        self.dict[doc_id] = doc_obj
