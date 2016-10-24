import logging
from logging import INFO
from unittest import TestLoader
from unittest import TextTestRunner
from unittest import TestSuite
from test.TestInMemoryDocumentStore import TestInMemoryDocumentStore
from test.TestInMemoryInvertedIndex import TestInMemoryInvertedIndex

class TestOrcas:

    def main(self):
        logging.getLogger().setLevel(level=INFO)
        test_document_store_suite_p0 = TestSuite(TestLoader().loadTestsFromTestCase(TestInMemoryDocumentStore))
        test_inverted_index_suite_p0 = TestSuite(TestLoader().loadTestsFromTestCase(TestInMemoryInvertedIndex))

        test_runner = TextTestRunner(verbosity = 2)
        test_runner.run(test_document_store_suite_p0)
        test_runner.run(test_inverted_index_suite_p0)

if __name__ == '__main__':
    TestOrcas().main()