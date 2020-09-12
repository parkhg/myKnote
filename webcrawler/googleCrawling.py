# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print(counts)


import requests
from bs4 import BeautifulSoup
r = requests.get('https://sneakernews.com/category/adidas')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.post-content > h4 > a')
for title in titles:
    print(title.text)