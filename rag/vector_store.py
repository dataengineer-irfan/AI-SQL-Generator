import pickle
from pathlib import Path

import faiss
import numpy as np


class VectorStore:

    def __init__(
        self,
        index_path: str = "vector_store/schema.index",
        metadata_path: str = "vector_store/schema_metadata.pkl"
    ):

        self.index_path = index_path
        self.metadata_path = metadata_path

        Path("vector_store").mkdir(
            exist_ok=True
        )

    def save(
        self,
        embeddings,
        documents
    ):

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(
            dimension
        )

        index.add(
            embeddings
        )

        faiss.write_index(
            index,
            self.index_path
        )

        with open(
            self.metadata_path,
            "wb"
        ) as file:

            pickle.dump(
                documents,
                file
            )

    def build(
        self,
        documents,
        embeddings
    ):
        """
        Compatibility wrapper.
        Older modules call build().
        Internally uses save().
        """

        self.save(
            embeddings,
            documents
        )

    def load(self):

        if not Path(
            self.index_path
        ).exists():

            raise FileNotFoundError(
                f"Index not found: {self.index_path}"
            )

        if not Path(
            self.metadata_path
        ).exists():

            raise FileNotFoundError(
                f"Metadata not found: {self.metadata_path}"
            )

        index = faiss.read_index(
            self.index_path
        )

        with open(
            self.metadata_path,
            "rb"
        ) as file:

            documents = pickle.load(
                file
            )

        return index, documents

    def search(
        self,
        query_embedding,
        top_k: int = 5
    ):

        index, documents = self.load()

        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx < len(documents):

                results.append(
                    documents[idx]
                )

        return results