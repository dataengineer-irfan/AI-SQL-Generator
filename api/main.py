import time

from fastapi import FastAPI, HTTPException

from api.models.request_models import SQLRequest
from api.models.response_models import SQLResponse

from generation.enhanced_sql_generator import (
    EnhancedSQLGenerator
)

from execution.dataset_sql_executor import (
    DatasetSQLExecutor
)

from logging_system.json_logger import (
    JSONLogger
)

app = FastAPI(
    title="AI SQL Generator",
    version="1.0.0",
    description="Enterprise AI Text-to-SQL Platform"
)

generator = EnhancedSQLGenerator()

executor = DatasetSQLExecutor()

logger = JSONLogger()

DATASET = (
    "datasets/sample-sales-data/"
    "sales_data_sample.csv"
)


@app.get("/")
def home():

    logger.info(
        "Home endpoint called",
        module="api"
    )

    return {
        "message": "AI SQL Generator API",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():

    logger.info(
        "Health endpoint called",
        module="api"
    )

    return {
        "status": "Healthy",
        "service": "AI SQL Generator",
        "version": "1.0.0"
    }


@app.post(
    "/generate",
    response_model=SQLResponse
)
def generate_sql(request: SQLRequest):

    start = time.time()

    try:

        logger.info(
            "Generate request received",
            module="api",
            question=request.question
        )

        sql = generator.generate(
            request.question,
            ""
        )

        logger.info(
            "SQL generated",
            module="generator",
            sql=sql
        )

        results = executor.execute(
            sql,
            DATASET
        )

        elapsed = round(
            time.time() - start,
            3
        )

        logger.info(
            "SQL executed successfully",
            module="execution",
            row_count=len(results),
            execution_time=elapsed
        )

        response = SQLResponse(

            question=request.question,

            sql=sql,

            execution_time=elapsed,

            row_count=len(results),

            results=results.to_dict(
                orient="records"
            )

        )

        logger.info(
            "Response returned successfully",
            module="api"
        )

        return response

    except Exception as ex:

        logger.error(
            "API execution failed",
            module="errors",
            exception=ex,
            question=request.question
        )

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )