import os
import pandas as pd


class MetadataIndexer:

    def build_metadata(
        self,
        dataset_path: str
    ):

        metadata = []

        for root, dirs, files in os.walk(
            dataset_path
        ):

            for file in files:

                if file.lower().endswith(".csv"):

                    full_path = os.path.join(
                        root,
                        file
                    )

                    try:

                        try:

                            df = pd.read_csv(
                                full_path,
                                nrows=5,
                                encoding="utf-8"
                            )

                        except UnicodeDecodeError:

                            df = pd.read_csv(
                                full_path,
                                nrows=5,
                                encoding="latin1"
                            )

                        metadata.append(
                            {
                                "file": file,
                                "path": full_path,
                                "columns": list(
                                    df.columns
                                ),
                                "rows_preview":
                                    df.head(3).to_dict()
                            }
                        )

                    except Exception as ex:

                        print(
                            f"Skipped {file}: {ex}"
                        )

        return metadata