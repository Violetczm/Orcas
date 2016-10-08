#! /usr/bin/env python

from util import NLProcessor


class InvertedIndex(object):
    """
    Interface - This is a dictionary of term to document id.
    """

    def get_postings(self, term):
        raise NotImplementedError('InvertedIndexes must be implemented with get_index()')

    def set_postings(self, term, postings):
        raise NotImplementedError('InvertedIndexes must be implemented with set_index()')


class InMemoryInvertedIndex(InvertedIndex):
    def __init__(self, doc_store, redis_client_params=None):
        self.inverted_indexes_map = TermToPostingsMap()
        self.doc_store = doc_store

    def __str__(self):
        return str(self.inverted_indexes_map)

    def get_postings(self, term):
        return self.inverted_indexes_map[term]

    def set_postings(self, term, postings):
        self.inverted_indexes_map[term] = postings

    def index_terms(self):
        """
        index the normalized terms in a document into inverted indexes map
        """
        [[self.set_postings(term, id) for term in NLProcessor.process(doc)] for id, doc in
         self.doc_store.dict.iteritems()]


class TermToPostingsMap(dict):
    """
    A map to store the inverted index, where key = term, value = a set of document ids
    """

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, key, value):
        """
        Upsert
        """
        dict.__setitem__(self, key, self[key] | set(value) if key in self else set(value))

    def __str__(self):
        return '\n'.join([k + ' = ' + ','.join(v) for k, v in self.iteritems()])
