from rag.embeddings import EmbeddingModel
from rag.retriever import Retriever
from rag.schema_loader import SchemaLoader
from rag.vector_store import VectorStore


class RAGPipeline:

    def __init__(self):

        self.loader = SchemaLoader()

        self.embedding_model = (
            EmbeddingModel()
        )

        self.vector_store = (
            VectorStore()
        )

    def build_index(self):

        documents = (
            self.loader.build_documents()
        )

        embeddings = (
            self.embedding_model.embed_batch(
                documents
            )
        )

        self.vector_store.save(
            embeddings,
            documents
        )

        return len(documents)

    def retrieve(
        self,
        question: str,
        top_k: int = 5
    ):

        retriever = Retriever()

        return retriever.retrieve(
            question,
            top_k
        )
