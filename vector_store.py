import math

class VectorStore:
    def __init__(self):
        self.vectors = []

    def embed(self, text):
        return [
            len(text),
            sum(ord(c) for c in text) % 1000
        ]

    def add(self, text, metadata):
        vec = self.embed(text)
        self.vectors.append((vec, metadata))

    def similarity(self, v1, v2):
        return 1 / (1 + math.dist(v1, v2))

    def search(self, query, top_k=5):
        query_vec = self.embed(query)

        results = []
        for vec, meta in self.vectors:
            score = self.similarity(query_vec, vec)
            results.append((score, meta))

        results.sort(reverse=True, key=lambda x: x[0])
        return [r[1] for r in results[:top_k]]