from log_settings import get_logger
from sample_class import SampleClass

logger = get_logger(__name__)

def run_sample():
    logger.debug("sample debug level log message")
    logger.info("sample info level log message")
    logger.warning("sample warning level log message")
    logger.error("sample error level log message")

    try:
        raise ValueError("error!")
    except ValueError as e:
        logger.exception(e)

    sc = SampleClass()
    sc.run_sample()

if __name__ == '__main__':
    run_sample()