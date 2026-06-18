from correction.sql_auto_corrector import (
    SQLAutoCorrector
)


def main():

    sql = """
SELECT CUSTOMER,
SUM(SALES)
FROM SALES_DATA_SAMPL
GROUP BY CUSTOMER
"""

    print("\nOriginal SQL\n")

    print(sql)

    corrector = (
        SQLAutoCorrector()
    )

    fixed = (
        corrector.correct(sql)
    )

    print("\nCorrected SQL\n")

    print(fixed)


if __name__ == "__main__":
    main()
