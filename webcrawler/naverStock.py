# encoding = UTF-8

"""

"""
import requests
import bs4

# Naver 증권사이트
vURL = "http://finance.naver.com/"


def run():
    resp = requests.get(vURL)
    resp.raise_for_status()
    resp.encoding = "euc-kr"        # 한글 인코딩
    html = resp.text

    bs = bs4.BeautifulSoup(html, "html.parser")
    tags = bs.select('div.news_area h2 a')      # Top News
    title = tags[0].getText()
    print(title)


if __name__ == '__main__':
    run()
