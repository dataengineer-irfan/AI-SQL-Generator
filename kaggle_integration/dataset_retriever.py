import numpy as np

from config.settings import settings
from rag.vector_store import VectorStore


class DatasetRetriever:

    def __init__(self):

        self.vector_store = VectorStore()

        if settings.ENABLE_RAG:

            from rag.embeddings import EmbeddingModel

            self.embedding_model = EmbeddingModel()

        else:

            self.embedding_model = None

    def retrieve(
        self,
        question: str,
        top_k: int = 3
    ):

        # Skip semantic retrieval when RAG is disabled
        if not settings.ENABLE_RAG:

            return []

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

            if (
                idx >= 0 and
                idx < len(docs)
            ):

                results.append(
                    docs[idx]
                )

        return results