from generation.sql_generator import SQLGenerator


def main():

    generator = SQLGenerator()

    question = (
        "Show total sales by customer"
    )

    sql = generator.generate(
        question
    )

    print("\nQuestion:\n")

    print(question)

    print("\nGenerated SQL:\n")

    print(sql)


if __name__ == "__main__":
    main()
