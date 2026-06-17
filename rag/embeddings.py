from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def embed_documents(
        self,
        documents
    ):

        return self.model.encode(
            documents,
            convert_to_numpy=True
        )

    def embed_query(
        self,
        query
    ):

        return self.model.encode(
            [query],
            convert_to_numpy=True
        )[0]

    # backward compatibility

    def encode(
        self,
        texts
    ):

        return self.embed_documents(
            texts
        )