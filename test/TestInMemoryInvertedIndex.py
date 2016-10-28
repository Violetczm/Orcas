import unittest
from unittest import TestCase
from docstore.DocumentStore import InMemoryDocumentStore
from invertedindex.InvertedIndex import InMemoryInvertedIndex


class TestInMemoryInvertedIndex(TestCase):
    def setUp(self):
        '''
        Set UP
        :return:
        '''
        TestCase.setUp(self)
        self.doc_store = InMemoryDocumentStore()
        self.doc_store.set_document('1', 'I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me')
        self.doc_store.set_document('2', 'So let it be with Caesar. The noble Brutus hath told you Caesar was ambitious:')
        self.doc_store.set_document('3',
                               'Some economists have responded positively to Bitcoin, including Francois R. Velde, ' + \
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

        self.inverted_index = InMemoryInvertedIndex(self.doc_store)

    def test_index_terms(self):
        self.inverted_index.index_terms()
        assert self.inverted_index.get_postings('Bitcoin') == set(['3']), 'Bitcoin should be in document 3, actual is %s' % self.inverted_index.get_postings('Bitcoin')
        assert self.inverted_index.get_postings('Caesar') == set(['1', '2']), 'Caesar should be in documents 1 and 2, actual is %s' % self.inverted_index.get_postings('Caesar')
        assert self.inverted_index.get_postings('Nick Colas') == set(['3']), 'Nick Colas should be in document 3, actual is %s' % self.inverted_index.get_postings('Nick Colas')
        assert self.inverted_index.get_postings('Julius Caesar') == set(['1']), 'Julius Caesar should be in document 1, actual is %s' % self.inverted_index.get_postings('Julius Caesar')

    def tearDown(self):
        '''
        Tear Down
        :return:
        '''
        TestCase.tearDown(self)
        self.doc_store = None
        self.inverted_index = None

if __name__ == '__main__':
    unittest.main()




