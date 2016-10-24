import unittest
from unittest import TestCase
from docstore.DocumentStore import InMemoryDocumentStore


class TestInMemoryDocumentStore(TestCase):
    def setUp(self):
        '''
        Set UP
        :return:
        '''
        TestCase.setUp(self)
        # Trying out code here:
        self.doc_store = InMemoryDocumentStore()

    def test_set_document(self):
        document_text = 'I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me'
        self.doc_store.set_document('1', document_text)
        assert self.doc_store.get_document('1') == document_text, 'Unable to set document'

    def tearDown(self):
        '''
        Tear Down
        :return:
        '''
        TestCase.tearDown(self)
        self.doc_store = None


if __name__ == '__main__':
    unittest.main()
