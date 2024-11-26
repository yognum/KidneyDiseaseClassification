from src import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Stage {STAGE_NAME} started")
    pipeline = DataIngestionPipeline()
    logger.info(f"Stage {STAGE_NAME} finished")
except Exception as e:
    logger.error(f"Getting exception on Stage {STAGE_NAME} with exception: {e}")
    raise e

