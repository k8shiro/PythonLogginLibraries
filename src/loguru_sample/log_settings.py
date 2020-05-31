from loguru import logger
import sys

def set_config():
    logger.remove()
    log_format = "<green>{time:YYYY-MM-DDTHH:mm:ss}</green>| {file} {line}: {module} {function}|<level>{level} {message}</level>"

    logger.add(
        "/var/log/loguru_sample2.log",
        rotation="12:00",
        format=log_format,
        enqueue=True
    )

    logger.add(
        sys.stderr,
        format=log_format
    )
