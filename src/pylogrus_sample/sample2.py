import logging
from pylogrus import PyLogrus, TextFormatter, JsonFormatter

logging.setLoggerClass(PyLogrus)

logger = logging.getLogger(__name__)  # type: PyLogrus
logger.setLevel(logging.DEBUG)


print("基本的な出力とファイルへの出力")
formatter = TextFormatter(datefmt='Z', colorize=True)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

ch = logging.FileHandler('/var/log/py_logrus_sample2.log')
ch.setLevel(logging.ERROR)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug("DEBUG MESSAGE")
logger.info("INFO MESSAGE")
logger.warning("WARNING MESSAGE")
logger.error("ERROR MESSAGE")

print("メッセージにPrefixをつける")
logger = logger.withPrefix("[API]")
logger.debug("DEBUG MESSAGE")

print("メッセージにフィールドを追加する")
logger.withFields({'error_code': 404}).info("INFO MESSAGE")


print("JSON形式で出力")
logger = logging.getLogger(__name__) 
enabled_fields = [
    ('name', 'logger_name'),
    ('asctime', 'service_timestamp'),
    ('levelname', 'level'),
    ('threadName', 'thread_name'),
    'message',
    ('exception', 'exception_class'),
    ('stacktrace', 'stack_trace'),
    'module',
    ('funcName', 'function')
]
formatter = JsonFormatter(datefmt='Z', enabled_fields=enabled_fields, indent=2, sort_keys=True)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug("DEBUG MESSAGE")
logger.info("INFO MESSAGE")
logger.warning("WARNING MESSAGE")
logger.error("ERROR MESSAGE")

