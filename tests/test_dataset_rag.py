from kaggle_integration.dataset_retriever import (
    DatasetRetriever
)


def main():

    retriever = (
        DatasetRetriever()
    )

    results = retriever.retrieve(
        "sales by country"
    )

    print("\nRetrieved Documents\n")

    for doc in results:

        print(doc)

        print(
            "\n" +
            "-" * 50 +
            "\n"
        )


if __name__ == "__main__":
    main()
