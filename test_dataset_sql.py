from rag.rag_pipeline import (
    RAGPipeline
)

from generation.enhanced_sql_generator import (
    EnhancedSQLGenerator
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

    print(
        "\nGenerated SQL\n"
    )

    print(sql)


if __name__ == "__main__":
    main()
