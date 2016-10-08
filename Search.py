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
    doc_store.set_document('3', 'Some economists have responded positively to Bitcoin, including Francois R. Velde, ' + \
                           'senior economist of the Federal Reserve in Chicago who described it as "an elegant solution ' + \
                           'to the problem of creating a digital currency." In November 2013 Richard Branson' + \
                           ' announced that Virgin Galactic would accept Bitcoin as payment, saying that ' + \
                           'he had invested in Bitcoin and found it "fascinating how a whole new global ' + \
                           'currency has been created", encouraging others to also invest in Bitcoin.  Other economists ' + \
                           'commenting on Bitcoin have been critical.  Economist Paul Krugman has suggested that the ' + \
                           'structure of the currency incentivizes hoarding and that its value derives from the expectation ' + \
                           'that others will accept it as payment. Economist Larry Summers has expressed a "wait and see" attitude ' + \
                           'when it comes to Bitcoin. Nick Colas, a market strategist for ConvergEx Group, has remarked on the effect ' + \
                           'of increasing use of Bitcoin and its restricted supply, noting, "When incremental adoption meets relatively ' + \
                           'fixed supply, it should be no surprise that prices go up. And that\'s exactly what is happening to BTC prices."')

    inverted_index = InMemoryInvertedIndex(doc_store)
    inverted_index.index_terms()

    print inverted_index
