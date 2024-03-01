from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summarizer.logging import logger


Stage_name = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {Stage_name} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {Stage_name} completed <<<<\n\nX==================X")
except Exception as e:
    logger.exception(e)
    raise e


Stage_name = "Data Validaion Stage"
try: 
    logger.info(f">>>> stage {Stage_name} started <<<<")
    data_validaion = DataValidationTrainingPipeline()
    data_validaion.main()
    logger.info(f">>>> stage {Stage_name} completed <<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e


Stage_name = "Data Transformation Stage"
try: 
    logger.info(f">>>> stage {Stage_name} started <<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {Stage_name} completed <<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e