import logging
import logging.config
import time

str_log_file_name = "my.log"
logging.config.fileConfig("logging.conf", disable_existing_loggers=False, defaults={"str_log_file_name" : str_log_file_name})
# disable_existing_loggers=False: 기 존재 로거도 계속 사용하도록 한다
logger = logging.getLogger("log03")

def function1():
    logger.info('haha...')
    time.sleep(20)

for i in range(99):
    function1()