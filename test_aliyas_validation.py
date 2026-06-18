from validation.dataset_validator import DatasetValidator

validator = DatasetValidator()

queries = [

    # Valid
    """
    SELECT s.COUNTRY,
           SUM(s.SALES)
    FROM SALES_DATA_SAMPLE s
    GROUP BY s.COUNTRY
    """,

    # Invalid alias
    """
    SELECT c.COUNTRY
    FROM SALES_DATA_SAMPLE s
    """,

    # Reserved keyword alias
    """
    SELECT OR.COUNTRY
    FROM SALES_DATA_SAMPLE OR
    """,

    # Another reserved keyword
    """
    SELECT AS.COUNTRY
    FROM SALES_DATA_SAMPLE AS
    """
]

for i, sql in enumerate(queries, start=1):

    print(f"\nTest {i}")

    print(
        validator.validate(sql)
    )
