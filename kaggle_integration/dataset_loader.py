import os
import zipfile
import kaggle


class DatasetLoader:

    def download_dataset(
        self,
        dataset_name: str,
        output_dir: str = "datasets"
    ):

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        kaggle.api.dataset_download_files(
            dataset_name,
            path=output_dir,
            unzip=True
        )

        return output_dir
