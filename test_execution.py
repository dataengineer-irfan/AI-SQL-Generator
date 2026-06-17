from generation.sql_generator import SQLGenerator

from validation.sql_validator import (
    SQLValidator
)

from evaluation.sql_score import (
    SQLScorer
)

from execution.sql_executor import (
    SQLExecutor
)


def main():

    question = (
        "Show total sales by customer"
    )

    generator = SQLGenerator()

    sql = generator.generate(
        question
    )

    print("\nGenerated SQL\n")

    print(sql)

    validator = SQLValidator()

    validation = (
        validator.validate(sql)
    )

    print("\nValidation\n")

    print(validation)

    scorer = SQLScorer()

    score = scorer.score(
        validation
    )

    print("\nScore\n")

    print(score)

    if score["score"] < 80:

        print(
            "\nExecution Blocked"
        )

        return

    executor = SQLExecutor()

    results = executor.execute(
        sql
    )

    print("\nResults\n")

    print(results)


if __name__ == "__main__":
    main()
