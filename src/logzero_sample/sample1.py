from logzero import setup_logger
from log_settings import DEFAULT_LOG_SETTINGS
from sample_class import SampleClass

logger = setup_logger(name=__name__, **DEFAULT_LOG_SETTINGS)

def run_sample():
    logger.debug("sample class debug level log message")
    logger.info("sample class info level log message")
    logger.warning("sample class warning level log message")
    logger.error("sample class error level log message")

    try:
        raise ValueError("error!")
    except ValueError as e:
        logger.exception(e)

    sc = SampleClass()
    sc.run_sample()

if __name__ == '__main__':
    run_sample()