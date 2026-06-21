import time
import traceback

from fastapi import FastAPI, HTTPException

from api.models.request_models import SQLRequest
from api.models.response_models import SQLResponse

from config.settings import settings
from logging_system.json_logger import JSONLogger

app = FastAPI(
    title="AI SQL Generator",
    version="1.0.0",
    description="Enterprise AI Text-to-SQL Platform"
)

logger = JSONLogger()

generator = None
executor = None

DATASET = (
    "datasets/sample-sales-data/"
    "sales_data_sample.csv"
)


@app.on_event("startup")
def startup():

    print("=" * 60)
    print("API STARTED")
    print(f"ENABLE_RAG = {settings.ENABLE_RAG}")
    print("=" * 60)


def get_generator():

    global generator

    if generator is None:

        logger.info(
            "Creating EnhancedSQLGenerator",
            module="api"
        )

        print("Creating EnhancedSQLGenerator...")

        from generation.enhanced_sql_generator import (
            EnhancedSQLGenerator
        )

        generator = EnhancedSQLGenerator()

        print("EnhancedSQLGenerator created.")

        logger.info(
            "EnhancedSQLGenerator created",
            module="api"
        )

    return generator


def get_executor():

    global executor

    if executor is None:

        logger.info(
            "Creating DatasetSQLExecutor",
            module="api"
        )

        print("Creating DatasetSQLExecutor...")

        from execution.dataset_sql_executor import (
            DatasetSQLExecutor
        )

        executor = DatasetSQLExecutor()

        print("DatasetSQLExecutor created.")

        logger.info(
            "DatasetSQLExecutor created",
            module="api"
        )

    return executor


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

        print("=" * 60)
        print("POST /generate received")
        print(f"Question: {request.question}")

        logger.info(
            "Generate request received",
            module="api",
            question=request.question
        )

        print("STEP 1 - Loading generator")

        sql = get_generator().generate(
            request.question,
            ""
        )

        print("STEP 2 - SQL generated")
        print(sql)

        logger.info(
            "SQL generated",
            module="generator",
            sql=sql
        )

        print("STEP 3 - Loading executor")

        results = get_executor().execute(
            sql,
            DATASET
        )

        print("STEP 4 - SQL executed")

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

        print("STEP 5 - Returning response")

        logger.info(
            "Response returned successfully",
            module="api"
        )

        return response

    except Exception as ex:

        print("\n========== EXCEPTION ==========")
        traceback.print_exc()
        print("========== END EXCEPTION ==========\n")

        logger.error(
            "API execution failed",
            exception=ex,
            module="errors",
            question=request.question
        )

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )