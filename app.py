from database.oracle_connector import OracleConnector
from database.schema_extractor import SchemaExtractor
from providers.groq_provider import GroqProvider


def oracle_health():

    connector = OracleConnector()

    connection = connector.connect()

    if connection is None:
        raise RuntimeError("Oracle connection failed")

    return True


def schema_health():

    extractor = SchemaExtractor()

    tables = extractor.get_tables()

    return len(tables)


def groq_health():

    provider = GroqProvider()

    response = provider.generate(
        "Reply with exactly: QWEN3_READY"
    )

    return response


def main():

    print("\nEnterprise Oracle Text-to-SQL Platform\n")

    print("Checking Oracle Connection...")

    oracle_health()

    print("✓ Oracle Connected")

    print("\nExtracting Schema...")

    table_count = schema_health()

    print(f"✓ Tables Discovered: {table_count}")

    print("\nChecking Groq...")

    result = groq_health()

    print(f"✓ Model Response: {result}")

    print("\nSystem Initialization Complete")

    extractor = SchemaExtractor()

    schema = extractor.extract_schema()

    print("\nBusiness Schema Loaded\n")

    for table_name in schema.keys():
        print(f"✓ {table_name}")


if __name__ == "__main__":
    main()
