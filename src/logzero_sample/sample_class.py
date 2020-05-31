from logzero import setup_logger
from log_settings import DEFAULT_LOG_SETTINGS

logger = setup_logger(name=__name__, **DEFAULT_LOG_SETTINGS)

class SampleClass():
    def run_sample(self):
        logger.debug("sample class debug level log message")
        logger.info("sample class info level log message")
        logger.warning("sample class warn level log message")
        logger.error("sample class error level log message")

        try:
            raise ValueError("error!")
        except ValueError as e:
            logger.exception(e)
