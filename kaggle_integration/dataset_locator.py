import os


class DatasetLocator:

    def find_csv(
        self,
        dataset_folder="datasets"
    ):

        for root, dirs, files in os.walk(
            dataset_folder
        ):

            for file in files:

                if file.endswith(".csv"):

                    return os.path.join(
                        root,
                        file
                    )

        return None
