from typing import List, Dict, Any

from pydantic import BaseModel


class SQLResponse(BaseModel):

    question: str

    sql: str

    execution_time: float

    row_count: int

    results: List[Dict[str, Any]]