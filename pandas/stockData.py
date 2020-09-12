# encoding = UTF-8

"""

출처: https://wendys.tistory.com/174 [웬디의 기묘한 이야기]
"""
import pandas_datareader as pdr
from datetime import datetime       # 일정기간 주식데이타를 가져오기 위해

dtstart = datetime(2018, 1, 1)
dtend   = datetime(2020, 9, 6)

# yahoo로 부터 데이타를 가져옴
df = pdr.DataReader("005930.KS", "yahoo", dtstart, dtend)

print(df)


def run():
    print("run")


if __name__ == '__main__':
    run()
