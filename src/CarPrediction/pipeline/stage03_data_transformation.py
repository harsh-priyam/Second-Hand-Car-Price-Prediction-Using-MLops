from CarPrediction.config.configuration import ConfigurationManager
from CarPrediction.components.data_transformation import DataTransformation
from CarPrediction import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e