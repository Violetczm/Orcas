#! /usr/bin/env python

from string import punctuation, whitespace


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

    def tokenize_doc(self, document):
        return set(term.lower() for term in document.split())

    def process_linquistics(self, terms):
        """
        Normalize terms to be meaningful words (not any versions of "be" and not "be", and single letters)
        """

        s_filter_list = ['is', 'was', 'are', 'were', 'be', 'been', 'has', 'have', 'had', 'not', 'isnt', 'wasnt',
                         'arnt',
                         'werent', 'hasnt', 'havent', 'hadnt']

        # remove punctuations and whitespaces
        normalized_terms = [str(t).translate(None, punctuation).translate(None, whitespace) for t in terms]
        # filter single letters
        filtered_singulars = filter(lambda x: len(x) > 1, normalized_terms)
        # filter out any versions of "be" and not "be", and return
        return set(filtered_singulars) - set(s_filter_list)

    def index_terms(self):
        """
        index the normalized terms in a document into inverted indexes map
        """
        [[self.set_postings(term, id) for term in self.process_linquistics(self.tokenize_doc(doc))] for id, doc in
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
