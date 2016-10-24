class TribalRanker:
    def __init__(self, inverted_index, doc_store, nl_processor):
        self.inverted_index = inverted_index
        self.doc_store = doc_store
        self.nl_processor = nl_processor


    def maping_docs_to_terms(self, docs_to_terms_map, doc_ids, term):
        map(lambda id: docs_to_terms_map.__setitem__(id, docs_to_terms_map[id] | set(
            term) if id in docs_to_terms_map else set(term)), doc_ids)
        return docs_to_terms_map

    def calculate_scores(self, docs_to_terms_map, total_counts):
        map = {}
        rate = float(1 / total_counts)
        return map(lambda id: map.__setitem__(id, 1.0 if len(docs_to_terms_map[id]) == total_counts else rate * len(
            docs_to_terms_map[id])), docs_to_terms_map.keys())

    def basic_rank(self, text):
        # normaliz the querying text (remove stop words)
        normalized_terms = self.nl_processor.process(text)

        # map each term to its postings (doc_ids)
        term_to_docs_map = {}
        map(lambda term: term_to_docs_map.__setitem__(term, self.inverted_index.get_postings(term)), normalized_terms)

        # map each posting (doc_id) to number of terms the document contains
        docs_to_terms_map = {}
        map(lambda (term, doc_ids): self.maping_docs_to_terms(docs_to_terms_map, doc_ids, term), term_to_docs_map.iteritems())

        # calculate each posting's ranking/scores of matching
        return self.calculate_scores(docs_to_terms_map, len(normalized_terms))
