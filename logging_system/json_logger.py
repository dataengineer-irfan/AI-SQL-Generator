import json
import os
import traceback
from datetime import datetime

from config.settings import settings


class JSONLogger:

    def __init__(self):

        os.makedirs(
            settings.LOG_DIR,
            exist_ok=True
        )

    def log(
        self,
        filename: str,
        payload: dict
    ):

        payload["timestamp"] = datetime.utcnow().isoformat()

        filepath = os.path.join(
            settings.LOG_DIR,
            f"{filename}.json"
        )

        with open(
            filepath,
            "a",
            encoding="utf-8"
        ) as f:

            json.dump(
                payload,
                f,
                ensure_ascii=False
            )

            f.write("\n")

    # --------------------------------------------------
    # INFO
    # --------------------------------------------------

    def info(
        self,
        category: str,
        message: str,
        **kwargs
    ):

        self.log(
            "application",
            {
                "level": "INFO",
                "category": category,
                "message": message,
                **kwargs
            }
        )

    # --------------------------------------------------
    # ERROR
    # --------------------------------------------------

    def error(
        self,
        category: str,
        message: str,
        exception=None,
        **kwargs
    ):

        self.log(
            "application",
            {
                "level": "ERROR",
                "category": category,
                "message": message,
                "exception": str(exception) if exception else None,
                "traceback": traceback.format_exc() if exception else None,
                **kwargs
            }
        )