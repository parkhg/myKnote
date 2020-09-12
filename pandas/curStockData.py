# encoding = UTF-8

"""

"""
import logging
import sqlite3
import pandas as pd
import time
from urllib.error import HTTPError
from urllib.request import urlopen
from tqdm import tqdm

from bs4 import BeautifulSoup


def get_sise(stock_code, try_cnt):
    try:
        url = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code={}".format(
            stock_code)
        req = urlopen(url)
        result = req.read()
        xmlsoup = BeautifulSoup(result, "lxml-xml")
        stock = xmlsoup.find("TBL_StockInfo")

        print(stock)

        stock_df = pd.DataFrame(stock.attrs, index=[0])
        stock_df = stock_df.applymap(lambda x: x.replace(",", ""))

        return stock_df
    except HTTPError as e:
        logging.warning(e)
        if try_cnt >= 3:
            return None
        else:
            get_sise(stock_code, try_cnt=+1)


# 주식 시세 DB에 저장하기
# con = sqlite3.connect("./data/div.db")
stock_code = ['005930', '066570']

for s in tqdm(stock_code):
    temp = get_sise(s, 1)
    # temp.to_sql(con=con, name="div_stock_sise", if_exists="append")
    time.sleep(0.5)
    print(temp)
# con.close()


def run():
    print("run")


if __name__ == '__main__':
    run()
