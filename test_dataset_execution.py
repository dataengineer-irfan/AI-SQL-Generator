from rag.rag_pipeline import RAGPipeline

from generation.enhanced_sql_generator import (
    EnhancedSQLGenerator
)

from execution.dataset_sql_executor import (
    DatasetSQLExecutor
)

from kaggle_integration.dataset_locator import (
    DatasetLocator
)


def main():

    question = (
        "Show total sales by country"
    )

    rag = RAGPipeline()

    schema_context = (
        rag.retrieve(
            question
        )
    )

    generator = (
        EnhancedSQLGenerator()
    )

    sql = generator.generate(
        question,
        schema_context
    )

    print("\nGenerated SQL\n")
    print(sql)

    locator = DatasetLocator()

    csv_path = (
        locator.find_csv()
    )

    print("\nDataset\n")
    print(csv_path)

    executor = (
        DatasetSQLExecutor()
    )

    results = executor.execute(
        sql,
        csv_path
    )

    print("\nResults\n")
    print(results.head())


if __name__ == "__main__":
    main()
