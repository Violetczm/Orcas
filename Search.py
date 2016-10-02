#! /usr/bin/env python
from docstore.DocumentStore import InMemoryDocumentStore
from invertedindex.InvertedIndex import InMemoryInvertedIndex

class Search:
    """
    Main class to peform search.
    """
    pass


if __name__ == '__main__':

    # Trying out code here:
    doc_store = InMemoryDocumentStore()
    doc_store.set_document('1', 'I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me')
    doc_store.set_document('2', 'So let it be with Caesar. The noble Brutus hath told you Caesar was ambitious:')

    inverted_index = InMemoryInvertedIndex(doc_store)
    inverted_index.index_terms()

    print inverted_index