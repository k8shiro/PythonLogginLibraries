import logzero
import logging

from logzero import logger

logzero.loglevel(logging.DEBUG)

logzero.logfile(
    '/var/log/logzero_sample2.log',
    loglevel=logging.ERROR,
    maxBytes=1e6,
    backupCount=3
)

#log_format = '%(color)s[%(levelname)1.1s %(asctime)s %(name)s %(module)s %(funcName)s:%(lineno)d]%(end_color)s %(message)s'
#formatter = logzero.LogFormatter(fmt=log_format)
#logzero.formatter(formatter)

logger.debug("sample debug level log message")
logger.info("sample info level log message")
logger.warning("sample warning level log message")
logger.error("sample error level log message")

try:
    raise ValueError("error!")
except ValueError as e:
    logger.exception(e)