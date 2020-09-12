# encoding = UTF-8

"""

"""
# myMain.py
import logging
import logexample.myMainLib

# 공통 Log Class 이용
from logexample import log_conf

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    logexample.myMainLib.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    logger = log_conf.Logger(__name__)
    logger.info("Logger Class Test!!!")

    main()
