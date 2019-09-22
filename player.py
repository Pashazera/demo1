# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://csgo.5eplay.com/data/rank/player'
#
# resqonse = requests.get(url)
# content = resqonse.content
# soup = BeautifulSoup(content,'lxml')
# datalist = soup.findAll(name='tr',attrs={'class':'tr-record font-industry odd'})
# datalist1 = soup.findAll(name='tr')
#
# print(datalist1)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq


def get_page(url):
    """发起请求 获得源码"""
    r = requests.get(url)
    r.encoding = 'utf8'
    html = r.text
    return html


def parse(text):
    """解析数据 写入文件"""
    doc = pq(text)
    # 获得每一行的tr标签
    tds = doc('table.table tbody tr.alt').items()
    for td in tds:
        rank = td.find('td:first-child').text()     # 排名
        name = td.find('div').text()  # 大学名称
        city = td.find('td:nth-child(3)').text()    # 城市
        score = td.find('td:nth-child(4)').text()   # 总分
        with open('college.csv', 'a+', encoding='utf8') as f:
            f.write(rank + '\t\t')
            f.write(name + '\t\t')
            f.write(city + '\t\t')
            f.write(score + '\t\t\n')
    print("写入完成")

def parse1(text):
    doc = pq(text)
    tds = doc()

if __name__ == "__main__":
    url = "https://csgo.5eplay.com/data/rank/player"
    text = get_page(url)
    print(text)
   # parse(text)
