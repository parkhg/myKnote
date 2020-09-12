# encoding = UTF-8
import os
import logging
import logging.handlers

# 1. 로거 인스턴스를 만든다
logger = logging.getLogger('mylogger')

# 1-1. 포매터를 만든다
fomatter = logging.Formatter('[%(filename)s:%(lineno)s:%(levelname)s] %(asctime)s > %(message)s')

# 환경변수를 읽어서 로깅 레벨과 로그를 남길 파일의 경로를 변수에 저장한다

filename = '/tmp/test.log'

# 2. 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
fileHandler = logging.FileHandler(filename)
streamHandler = logging.StreamHandler()

# 2-1.각 핸들러에 포매터를 지정한다.
fileHandler.setFormatter(fomatter)
streamHandler.setFormatter(fomatter)

# 3. 1번에서 만든 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# 4. 로거 인스턴스로 로그를 찍는다.
logger.setLevel(logging.DEBUG)
logger.debug("===========================")
logger.info("TEST START")
logger.warning("스트림으로 로그가 남아요~")
logger.error("파일로도 남으니 안심이죠~!")
logger.critical("치명적인 버그는 꼭 파일로 남기기도 하고 메일로 발송하세요!")
logger.debug("===========================")
logger.info("TEST END!")
