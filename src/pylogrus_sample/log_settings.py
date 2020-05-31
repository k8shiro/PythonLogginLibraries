import logging
from pylogrus import PyLogrus, TextFormatter
def get_logger(name):
    logging.setLoggerClass(PyLogrus)
    logger = logging.getLogger(name)  # type: PyLogrus
    logger.setLevel(logging.DEBUG)

    formatter = TextFormatter(datefmt='Z', colorize=True)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    ch = logging.FileHandler('/var/log/py_logrus_sample2.log')
    ch.setLevel(logging.ERROR)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
