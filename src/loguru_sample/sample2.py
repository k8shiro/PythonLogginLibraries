from loguru import logger
import sys

# デフォルトで使う
print("# デフォルトで使う")
from loguru import logger

logger.trace("sample trace level log message")
logger.debug("sample debug level log message")
logger.info("sample info level log message")
logger.warning("sample warn level log message")
logger.error("sample error level log message")
logger.critical("sample critical level log message")

# 基本的な使い方
print("# 基本的な使い方")
logger.remove()
log_format = "<green>{time:YYYY-MM-DDTHH:mm:ss}</green> <level>{level} {message}</level>"

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

# JSONで出力する
print("# JSONで出力する")
logger.remove()
log_format = "<green>{time}</green>: <level>{level} {message}</level>: {extra[extra_value]}"
logger.add(
    sys.stdout,
    format=log_format,
    serialize=True
)

logger.bind(extra_value="some_extra_value").info("serialize message 01")
logger.info("serialize message 02", extra_value="some_extra_value")


# logger.optのサンプル
print("# logger.optのサンプル")

## lazy
print("## lazy")
logger.remove()
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
def test_lazy():
    print('exec test_razy')
    return 'exec test_razy'
print('lazy=True')
logger.opt(lazy=True).debug("DEBUG LEVEL LOG: {x}", x=lambda: test_lazy())
print('lazy=False')
logger.opt(lazy=False).debug("DEBUG LEVEL LOG: {x}", x=test_lazy())

## exception
print("## exception")
logger.remove()
logger.add(sys.stderr, format="<green>{time}</green>: <level>{level} {message}</level>", level="INFO")
try:
    raise ValueError("error!")
except ValueError as e:
    logger.opt(exception=True).critical("Exceptionのloglevelを変える")

## colors
print("## colors")
logger.opt(colors=True).info("ログに色をつける <blue>colors</blue>")

## record
print("## record")
logger.opt(record=True).info("recordに格納されている情報をlogに付与する (eg. {record[thread]})")

## raw
print("## raw")
logger.opt(raw=True).info("フォーマットを無視してログ出力\n")


## depth
print("## depth")
logger.remove()
logger.add(sys.stderr, format="{time} {level} {message} {function}", level="INFO")
def child_func():
    logger.opt(depth=1).info("親の情報をログに表示する")

def parent_func():
    child_func()
parent_func()

## capture
print("## capture")
logger.remove()
logger.add(sys.stderr, format="{time} {level} {message} {function}", level="INFO", serialize=True)
logger.opt(capture=True).info("{dest} messageのみに変数を使用する", dest="extra")
