from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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


Stage_name = "Model Training Stage"
try: 
    logger.info(f">>>> stage {Stage_name} started <<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>> stage {Stage_name} completed <<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e


Stage_name = "Model Evaluation Stage"
try: 
    logger.info(f">>>> stage {Stage_name} started <<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>> stage {Stage_name} completed <<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e