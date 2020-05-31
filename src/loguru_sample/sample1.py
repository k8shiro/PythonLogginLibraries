from loguru import logger
from log_settings import set_config
from sample_class import SampleClass

set_config()


def run_sample():
    logger.trace("sample trace level log message")
    logger.debug("sample debug level log message")
    logger.info("sample info level log message")
    logger.warning("sample warn level log message")
    logger.error("sample error level log message")
    logger.critical("sample critical level log message")

    try:
        raise ValueError("error!")
    except ValueError as e:
        logger.exception(e)

    sc = SampleClass()
    sc.run_sample()

if __name__ == '__main__':
    run_sample()