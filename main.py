from CarPrediction import logger 
from CarPrediction.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from CarPrediction.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from CarPrediction.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from CarPrediction.pipeline.stage04_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Model Trainer stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e