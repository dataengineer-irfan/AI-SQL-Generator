from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class DatasetRAGBuilder:

    def __init__(self):

        self.embedding_model = (
            EmbeddingModel()
        )

        self.vector_store = (
            VectorStore()
        )

    def build(
        self,
        metadata
    ):

        if len(metadata) == 0:

            print(
                "No metadata found."
            )

            return 0

        docs = []

        for item in metadata:

            text = (
                f"FILE: {item['file']}\n"
                f"PATH: {item.get('path', '')}\n"
                f"COLUMNS: {item['columns']}\n"
                f"PREVIEW: {item.get('rows_preview', {})}"
            )

            docs.append(text)

        embeddings = (
            self.embedding_model.embed_documents(
                docs
            )
        )

        self.vector_store.save(
            embeddings,
            docs
        )

        print(
            f"Indexed {len(docs)} documents"
        )

        return len(docs)