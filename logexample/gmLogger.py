# encoding = UTF-8

"""
1. logging.conf 파일을 통해서 외부에서 설정 가능
2. 레벨을 자유롭게 설정하고 추가 할 수 있어야 한다.
   (CRITICAL < ERROR < WARNING[default] < INFO < DEBUG )

3. 파일,스트림에 동시에 출력 할 수 있어야 한다.
4. 다양한 목적에 따라 다양한 파일에 출력 할 수 있어야 한다.
5. 로깅 시간 출력 및 다양한 정보에 대한 추가가 가능해야 한다.
6. 하루에 한번씩 파일을 생성 해야하며, 지난 파일은 압축하여 보관 해야한다.
7. 하루에 한번씩 파일을 생성 해야하며, 오래된 파일을 삭제 할 수 있어야 한다.
8. 파일 용량이 너무 커질 경우에는 자동으로 분리 시켜야 한다.

9. 멀티프로세스를 활용해야 하는 파이썬의 특성상 멀티프로세스에서도 로그를 취득할 수 있어야 한다.

10. 핸들러를 커스터마이징 할 수 있어야 한다. 즉 콘솔,파일 출력 뿐 만 아니라, DB 및 소켓을 통하여도 발송 할 수 있어야 한다.
11. 사용하기 쉬워야 한다. (문서화가 잘 되 있어야 한다) , 기본 로깅 모듈을 사용해야한다.
"""
import logging


def run():
    pass

if __name__ == '__main__':
    mylogger = logging.getLogger(__name__)              # 1. 인스턴스 생성
    mylogger.setLevel(logging.INFO)                     # 2. 레벨설정

    formatter = logging.Formatter("%(asctime)s [%(name)-12s] %(levelname)-8s > %(message)s")     # 5.출력 포맷팅 설정

    streamhandler = logging.StreamHandler()             # 3. handler 설정
    streamhandler.setFormatter(formatter)               # 5.1 출력포맷팅 설
    mylogger.addHandler(streamhandler)

    filehandler = logging.FileHandler("my.log")         # 4. File 핸들러 설정
    mylogger.addHandler(filehandler)

    mylogger.info("server start")

    run()
