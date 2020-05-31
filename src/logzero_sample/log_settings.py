import logzero
import logging

log_format = '%(color)s[%(levelname)1.1s %(asctime)s %(name)s %(module)s %(funcName)s:%(lineno)d]%(end_color)s %(message)s'
formatter = logzero.LogFormatter(fmt=log_format)

DEFAULT_LOG_SETTINGS = {
    'logfile': '/var/log/logzero_sample1.log',
    'formatter': formatter,
    'maxBytes': 1000000,
    'backupCount': 3,
    'level': logging.DEBUG,
    'fileLoglevel': logging.ERROR,
}
