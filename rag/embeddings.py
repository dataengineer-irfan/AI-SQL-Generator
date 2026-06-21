from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2"
            )

        return cls._model

    def embed_documents(
        self,
        documents
    ):

        return self.get_model().encode(
            documents,
            convert_to_numpy=True
        )

    def embed_query(
        self,
        query
    ):

        return self.get_model().encode(
            [query],
            convert_to_numpy=True
        )[0]

    # Backward compatibility

    def encode(
        self,
        texts
    ):

        return self.embed_documents(
            texts
        )