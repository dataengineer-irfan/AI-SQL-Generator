from kaggle_integration.metadata_indexer import (
    MetadataIndexer
)

from kaggle_integration.rag_index_builder import (
    DatasetRAGBuilder
)


def main():

    indexer = MetadataIndexer()

    metadata = indexer.build_metadata(
        "datasets"
    )

    print("\nMETADATA COUNT:")
    print(len(metadata))

    print("\nFIRST 3 ITEMS:")

    for item in metadata[:3]:
        print(item)

    builder = DatasetRAGBuilder()

    count = builder.build(
        metadata
    )

    print(
        f"\nIndexed {count} dataset files"
    )


if __name__ == "__main__":
    main()