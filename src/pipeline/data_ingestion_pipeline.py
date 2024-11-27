import logging
from src.component.data_ingestion import DataIngestion

class DataIngestionPipeline:

    def __init__(self):
        pass

    def main(self):
        data_ingestion = DataIngestion()
        data_ingestion.download_file()
        data_ingestion.unzip_file()


try:
    logging.info(f"Data Ingestion process started.")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()

    logging.info(f"Data Ingestion process ended.")
except Exception as e:
    logging.error(f"Exception occurred: {e}")
    raise e
    

