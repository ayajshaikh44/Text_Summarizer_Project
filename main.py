from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from text_summarizer.logging import logger

Stage_name = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {Stage_name} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {Stage_name} completed <<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e