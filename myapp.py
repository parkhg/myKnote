# encoding = UTF-8

"""
APP Name : GoldMoon, 자동주식거래
Function
        1. 증권사 주식거래
        2. 거래내역 Msg Service
        3. Cron
        4. 데이타 수
Revision
        1. 2020.09.01 init version
Usage:
    Basic Echobot example, repeats messages.
    Press Ctrl-C on the command line or send a signal to the process to stop the
    bot.
"""
import os
import gmConfig
import logging
import logging.config
import json
import time


def logger_init():
    with open('logging.json', 'rt') as f:
        config = json.load(f)
        print(config)

    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info("Server Start")
    logger.debug("Debug Msg...")

    return logger


def run():
    # 환경변수 Read
    appEnv = gmConfig.Config("myapp.ini", debug=True)
    vAppNm = appEnv.getValue("APPLICATION", "appname")
    logger.info(vAppNm)

    # 환경변수 Update
    appEnv.setValue("APPLICATION", "OWNER", "baguju")
    appEnv.save()


def logtest():
    logger.info("GoldMoon...")
    time.sleep(20)


if __name__ == '__main__':
    logger = logger_init()

    run()

    for i in range(99):
        logtest()
