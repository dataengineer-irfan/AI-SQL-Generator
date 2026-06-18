from validation.auto_corrector import AutoCorrector


def main():

    validator = (
        AutoCorrector()
    )

    sql = """
    SELECT
        COUNTRY,
        SUM(SALES) AS TOTAL_SALES
    FROM
        SALES_DATA_SAMPLE
    GROUP BY
        COUNTRY
    """

    result = (
        validator.validate(sql)
    )

    print("\nValidation Result\n")

    print(result)


if __name__ == "__main__":
    main()
