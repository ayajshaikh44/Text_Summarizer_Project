from text_summarizer.components.data_validation import DataValidation
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validaion_config = config.get_data_validation_config()
            data_validaiton = DataValidation(config=data_validaion_config)
            data_validaiton.validation_all_file_exist()
        except Exception as e:
            raise e