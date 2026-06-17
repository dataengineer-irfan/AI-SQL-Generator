import numpy as np

from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding_model = (
            EmbeddingModel()
        )

        self.vector_store = (
            VectorStore()
        )

    def retrieve(
        self,
        question: str,
        top_k: int = 3
    ):

        query_embedding = (
            self.embedding_model.embed_query(
                question
            )
        )

        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        index, docs = (
            self.vector_store.load()
        )

        distances, indices = (
            index.search(
                query_embedding,
                top_k
            )
        )

        results = []

        for idx in indices[0]:

            if idx < len(docs):

                results.append(
                    docs[idx]
                )

        return results