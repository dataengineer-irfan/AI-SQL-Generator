from generation.sql_generator import SQLGenerator

from optimization.explain_plan import ExplainPlan
from optimization.index_recommender import (
    IndexRecommender
)
from optimization.sql_optimizer import (
    SQLOptimizer
)

from evaluation.sql_reviewer import (
    SQLReviewer
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

    plan_engine = ExplainPlan()

    plan = plan_engine.analyze(
        sql
    )

    print("\nExplain Plan\n")
    print(plan)

    recommender = (
        IndexRecommender()
    )

    indexes = (
        recommender.recommend(
            sql
        )
    )

    print("\nRecommended Indexes\n")

    for index in indexes:

        print(index)

    optimizer = (
        SQLOptimizer()
    )

    optimized_sql = (
        optimizer.optimize(
            question,
            sql,
            plan
        )
    )

    print("\nOptimized SQL\n")
    print(optimized_sql)

    reviewer = SQLReviewer()

    reviewed_sql = (
        reviewer.review(
            question,
            optimized_sql,
            {"score": 100},
            plan
        )
    )

    print("\nReviewed SQL\n")
    print(reviewed_sql)


if __name__ == "__main__":
    main()
