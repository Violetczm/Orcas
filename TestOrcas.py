import logging
from logging import INFO
from unittest import TestLoader
from unittest import TextTestRunner
from unittest import TestSuite
from test.TestInMemoryDocumentStore import TestInMemoryDocumentStore
from test.TestInMemoryInvertedIndex import TestInMemoryInvertedIndex
from test.TestTrivalRanker import TestTrivalRanker


class TestOrcas:
    def main(self):
        logging.getLogger().setLevel(level=INFO)
        test_loader = TestLoader()
        test_suites = [TestSuite(test_loader.loadTestsFromTestCase(TestInMemoryDocumentStore)),
                       TestSuite(test_loader.loadTestsFromTestCase(TestInMemoryInvertedIndex)),
                       TestSuite(test_loader.loadTestsFromTestCase(TestTrivalRanker))]

        test_runner = TextTestRunner(verbosity=2)
        map(lambda test_suite: test_runner.run(test_suite), test_suites)


if __name__ == '__main__':
    TestOrcas().main()
