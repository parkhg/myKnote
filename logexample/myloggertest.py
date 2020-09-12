# encoding = UTF-8

"""
    공통 Logger 호출
"""
from logexample import mylogger
logger = mylogger.getLogger(__name__)


def run():
    logger.debug("this is a debug message")
    logger.info("this is a info message...")


if __name__ == '__main__':
    run()
