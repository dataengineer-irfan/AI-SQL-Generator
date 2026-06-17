from typing import List

from database.schema_extractor import SchemaExtractor


class SchemaLoader:

    def __init__(self):
        self.extractor = SchemaExtractor()

    def build_documents(self) -> List[str]:
        schema = self.extractor.extract_schema()

        documents = []

        for table_name, table_data in schema.items():
            document = f"TABLE: {table_name}\n\n"
            document += "COLUMNS:\n"

            for column in table_data["columns"]:
                document += (
                    f"- {column['column_name']} "
                    f"{column['data_type']}\n"
                )

            documents.append(document)

        return documents
