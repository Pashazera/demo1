import pandas as pd
import numpy as np
import datetime
from pylab import *

# data = np.random.randn(8,5)
# index = pd.date_range('20190701',periods=8)
# columns = list('abcde')
# df = pd.DataFrame(data=data,columns=columns,index=index)
# print(df)
#
# print(columns)
#
# print(df[df.a>0][df.b>0])
# print(df[df>0])
# print(df>0)
#
# print(df[df.b.isin([1,2])])
#
# df['f'] = 1
# print(df)


#
# ts = pd.Series(data=np.random.rand(1000),index=pd.date_range('20100701',periods=1000))
# print(ts)
# ts = ts.cumsum()
# ts.plot()
# show()


# data = pd.read_excel('newNumber.xlsx')
# print(data)
#
#
#
# a = data.values[:,0]
# b = data.values[:,1]
#
# print(a)
# print(b)
# for x , y in zip(a,b):
#     print(x+y)
#
#
# c = pd.Series(a)
# print(c)
#
# print(c.isin([1,1]))


# df = pd.DataFrame(data=np.random.rand(8,3),columns=['一','二','三'])
# a = df['一']
# b = df['二']
#
# data = pd.DataFrame
# data['one'] = a.values
# data['two'] = b.values
# print(data)


# import tushare as ts
#
# import numpy as np
# import pandas as pd
# import math
# pd.set_option('display.max_columns',1000)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_colwidth',1000)
# data = pd.read_excel('data.xlsx')
# data = data[['促销品单价','费用金额']]
# print(data)
# data.columns=['product','amount']
#
# print(data)
#
#
# import tushare as ts
# ts.set_token('f49af853916324c3ffdbcd00c6c28db9e3ccc297943289e3aa96af55')
# pro = ts.pro_api('f49af853916324c3ffdbcd00c6c28db9e3ccc297943289e3aa96af55')
# pd.set_option('display.max_columns',1000)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_colwidth',1000)
# df = pro.film_record(start_date='20181014', end_date='20181214')
# print(df)
#
# print(ts.__version__)

# import time

# def test():
#     time.sleep(3)
#     print("this is test(),i sleep 3s")
#
#
# x = 1
# y = x
# z = lambda a:a**2
#
# def demo1(func):
#     start = time.time()
#     func()
#     stop = time.time()
#     print('demo is running{}'.format(start-stop))
#
# def demo2(func):
#     print(func)
#     return func

#既不需要侵入，也不需要函数重复执行
# import time
#
# def deco(func):
#     def wrapper(*args,**kwargs):
#         startTime = time.time()
#         func(*args,*kwargs)
#         endTime = time.time()
#         msecs = (endTime - startTime)*1000
#         print("time is %d ms" %msecs)
#     return wrapper
#
#
# @deco
# def func(a,b):
#     print("hello")
#     time.sleep(1)
#     print("world")
#     print('func({},{})'.format(a,b))
#
# @deco
# def func1(a,b,c):
#     print("hello")
#     time.sleep(1)
#     print("world")
#     print('func1({},{},{})'.format(a,b,c))
# if __name__ == '__main__':
#     func(1,2)
#     func1(1,2,3)


#多个装饰器

# import time
#
# def deco01(func):
#     def wrapper(*args, **kwargs):
#         print("this is deco01")
#         startTime = time.time()
#         func(*args, **kwargs)
#         endTime = time.time()
#         msecs = (endTime - startTime)*1000
#         print("time is %d ms" %msecs)
#         print("deco01 end here")
#     return wrapper
#
# def deco02(func):
#     def wrapper(*args, **kwargs):
#         print("this is deco02")
#         func(*args, **kwargs)
#
#         print("deco02 end here")
#     return wrapper
#
# @deco01
# @deco02
# def func(a,b):
#     print("hello，here is a func for add :")
#     time.sleep(1)
#     print("result is %d" %(a+b))
#     return a
#
#
# def adder(func):
#     def wrapper(*args,**kwargs):
#         print(args)
#         return func(*args,**kwargs)
#     return wrapper
#
# @adder
# def test(a,b):
#     return a+b
#
# if __name__ == '__main__':
#
#     print(test(1,2))
#
#
#

#
# from pyecharts.charts import Geo
# data = [
#     ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15),
#     ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
#     ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25),
#     ("文登", 25),("上海", 25),("攀枝花", 25),("威海", 25),("承德", 25),("厦门", 26),
#     ("汕尾", 26),("潮州", 26),("丹东", 27),("太仓", 27),("曲靖", 27),("烟台", 28),
#     ("福州", 29),("瓦房店", 30),("即墨", 30),("抚顺", 31),("玉溪", 31),("张家口", 31),
#     ("阳泉", 31),("莱州", 32),("湖州", 32),("汕头", 32),("昆山", 33),("宁波", 33),
#     ("湛江", 33),("揭阳", 34),("荣成", 34),("连云港", 35),("葫芦岛", 35),("常熟", 36),
#     ("东莞", 36),("河源", 36),("淮安", 36),("泰州", 36),("南宁", 37),("营口", 37),
#     ("惠州", 37),("江阴", 37),("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 38),
#     ("延安", 38),("太原", 39),("清远", 39),("中山", 39),("昆明", 39),("寿光", 40),
#     ("盘锦", 40),("长治", 41),("深圳", 41),("珠海", 42),("宿迁", 43),("咸阳", 43),
#     ("铜川", 44),("平度", 44),("佛山", 44),("海口", 44),("江门", 45),("章丘", 45),
#     ("肇庆", 46),("大连", 47),("临汾", 47),("吴江", 47),("石嘴山", 49),("沈阳", 50),
#     ("苏州", 50),("茂名", 50),("嘉兴", 51),("长春", 51),("胶州", 52),("银川", 52),
#     ("张家港", 52),("三门峡", 53),("锦州", 54),("南昌", 54),("柳州", 54),("三亚", 54),
#     ("自贡", 56),("吉林", 56),("阳江", 57),("泸州", 57),("西宁", 57),("宜宾", 58),
#     ("呼和浩特", 58),("成都", 58),("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
#     ("宜兴", 59),("北海", 60),("西安", 61),("金坛", 62),("东营", 62),("牡丹江", 63),
#     ("遵义", 63),("绍兴", 63),("扬州", 64),("常州", 64),("潍坊", 65),("重庆", 66),
#     ("台州", 67),("南京", 67),("滨州", 70),("贵阳", 71),("无锡", 71),("本溪", 71),
#     ("克拉玛依", 72),("渭南", 72),("马鞍山", 72),("宝鸡", 72),("焦作", 75),("句容", 75),
#     ("北京", 79),("徐州", 79),("衡水", 80),("包头", 80),("绵阳", 80),("乌鲁木齐", 84),
#     ("枣庄", 84),("杭州", 84),("淄博", 85),("鞍山", 86),("溧阳", 86),("库尔勒", 86),
#     ("安阳", 90),("开封", 90),("济南", 92),("德阳", 93),("温州", 95),("九江", 96),
#     ("邯郸", 98),("临安", 99),("兰州", 99),("沧州", 100),("临沂", 103),("南充", 104),
#     ("天津", 105),("富阳", 106),("泰安", 112),("诸暨", 112),("郑州", 113),("哈尔滨", 114),
#     ("聊城", 116),("芜湖", 117),("唐山", 119),("平顶山", 119),("邢台", 119),("德州", 120),
#     ("济宁", 120),("荆州", 127),("宜昌", 130),("义乌", 132),("丽水", 133),("洛阳", 134),
#     ("秦皇岛", 136),("株洲", 143),("石家庄", 147),("莱芜", 148),("常德", 152),("保定", 153),
#     ("湘潭", 154),("金华", 157),("岳阳", 169),("长沙", 175),("衢州", 177),("廊坊", 193),
#     ("菏泽", 194),("合肥", 229),("武汉", 273),("大庆", 279)]
# geo = Geo()
# attr, value = geo.cast(data)
# geo.add("", attr, data_pair=data, visual_range=[0, 200], maptype='china',visual_text_color="#fff",
#         symbol_size=10, is_visualmap=True)
# geo.render("全国主要城市空气质量.html")#生成html文件


# from pyecharts.charts import Bar
# from pyecharts.render import make_snapshot
#
# # 使用 snapshot-selenium 渲染图片
# from snapshot_selenium import snapshot
#
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# make_snapshot(snapshot, bar.render(), "bar.png")

#
# import pyecharts.charts as pychart
# from example.commons import Faker
# from pyecharts import options as opts
# from pyecharts.globals import ThemeType
# import numpy as np
#
# bar = pychart.Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
# x = list('abcde')
# y1 = [1,2,3,4,5]
# y2 = list(np.random.rand(5))
# y3 = list(np.array(np.arange(5)))
# print(y3)
# print(type(y3))
# bar.add_xaxis(x)
# bar.add_yaxis('biubiubiu',yaxis_data=y2)
# bar.add_yaxis('bar1',yaxis_data=y1)
# bar.set_global_opts(opts.TitleOpts(title='主标题',subtitle='副标题'))
# bar.render('bar.html')
#
# print(type(y1))
#
#


# import urllib.request as urlRequest
#
# from http import cookiejar
# url = 'https://www.baidu.com'
#
# print("funion 1")
# re1 = urlRequest.urlopen(url)
#
# print(re1.getcode())
# print(len(re1.read()))
#
# print('funion 2')
# request = urlRequest.Request(url)
# request.add_header('user-agent','Mozilla/5.0')
# re2 = urlRequest.urlopen(request)
# print(re2.getcode())
# print(len(re2.read()))

# import requests
# import urllib.request as ur
# from bs4 import BeautifulSoup
# BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
# PAGE_URL_LIST = []
# for i in range(1,3):
#     url = BASE_PAGE_URL + str(i)
#     PAGE_URL_LIST.append(url)
#
# response = requests.get('https://www.doutula.com/photo/list/?page=1')
# content = response.content
#
# soup = BeautifulSoup(content,'lxml')
# img_list = soup.findAll('img',attrs={'class':'img-responsive lazy image_dta'})
# print(img_list)
# for x in img_list:
#      print(x['data-original'])


#download
# url = 'http://img.doutula.com/production/uploads/image/2019/09/01/20190901322236_VNsohg.jpg'
#
# #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req = ur.Request(url)
# req.add_header('user-agent','Mozilla/5.0')
# #ur.urlretrieve(req,'test.jpg')
# re = ur.urlopen(req)
# print(re.getcode())
# r = requests.get(url)
# with open("code3.jpg", "wb") as code:
#      code.write(r.content)

#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# input = driver.find_element_by_css_selector('#kw')
# input.send_keys("苍老师照片")
#
# button = driver.find_element_by_css_selector('#su')
# button.click()

#
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import xlwt
#
# browser = webdriver.Chrome()
# WAIT = WebDriverWait(browser, 10)
# browser.set_window_size(1400, 900)
#
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#
# sheet = book.add_sheet('蔡徐坤篮球', cell_overwrite_ok=True)
# sheet.write(0, 0, '名称')
# sheet.write(0, 1, '地址')
# sheet.write(0, 2, '描述')
# sheet.write(0, 3, '观看次数')
# sheet.write(0, 4, '弹幕数')
# sheet.write(0, 5, '发布时间')
#
# n = 1
#
#
# def search():
#     try:
#         print('开始访问b站....')
#         browser.get("https://www.bilibili.com/")
#
#         # 被那个破登录遮住了
#         index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#primary_menu > ul > li.home > a")))
#         index.click()
#
#         input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner_link > div > div > form > input")))
#         submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))
#
#         input.send_keys('蔡徐坤 篮球')
#         submit.click()
#
#         # 跳转到新的窗口
#         print('跳转到新窗口')
#         all_h = browser.window_handles
#         browser.switch_to.window(all_h[1])
#         print('biu')
#         get_source()
#         print('getseource')
#         total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
#                                                            "#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.last > button")))
#         print(total)
#         return int(total.text)
#     except TimeoutException:
#         return search()
#
#
# def next_page(page_num):
#     try:
#         print('获取下一页数据')
#         next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                                           '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.next > button')))
#         next_btn.click()
#         WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
#                                                      '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.active > button'),
#                                                     str(page_num)))
#         get_source()
#     except TimeoutException:
#         browser.refresh()
#         return next_page(page_num)
#
#
# def save_to_excel(soup):
#     list = soup.find(class_='all-contain').find_all(class_='info')
#
#     for item in list:
#         item_title = item.find('a').get('title')
#         item_link = item.find('a').get('href')
#         item_dec = item.find(class_='des hide').text
#         item_view = item.find(class_='so-icon watch-num').text
#         item_biubiu = item.find(class_='so-icon hide').text
#         item_date = item.find(class_='so-icon time').text
#
#         print('爬取：' + item_title)
#
#         global n
#
#         sheet.write(n, 0, item_title)
#         sheet.write(n, 1, item_link)
#         sheet.write(n, 2, item_dec)
#         sheet.write(n, 3, item_view)
#         sheet.write(n, 4, item_biubiu)
#         sheet.write(n, 5, item_date)
#
#         n = n + 1
#
#
# def get_source():
#     WAIT.until(EC.presence_of_element_located(
#         (By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix')))
#     html = browser.page_source
#     soup = BeautifulSoup(html, 'lxml')
#     save_to_excel(soup)
#
#
# def main():
#     try:
#         total = search()
#         print(total)
#
#         for i in range(2, int(total + 1)):
#             next_page(i)
#
#     finally:
#         browser.close()
#
#
# if __name__ == '__main__':
#     main()
#     book.save(u'蔡徐坤篮球.xlsx')


# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.bilibili.com/video/av66370938'
#
# response = requests.get(url)
# content = response.content
#
# soup = BeautifulSoup(content,'lxml')
# data_list = soup.findAll(name='div',attrs={'class':'list-item reply-wrap '})
#
# print(data_list)

# import requests
# import json
#
# data = {'name':'pashazera','age':22}
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
#
# url = 'http://httpbin.org/get'
# url1 = 'http://www.jianshu.com'
# url2 = 'https://www.baidu.com/'
# response = requests.get(url1)
# print(response.url)
# print(response.headers)
# print(response.status_code)
# print(response.encoding)
#
# response = requests.get(url2)
# cookies = response.cookies
# for key,value in cookies.items():
#     print(key,value)


from bs4 import BeautifulSoup

html = '''

'''

'''
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
'''
soup = BeautifulSoup(html,'lxml')
# print(soup.prettify()) #自动补全html代码，格式化
# print(soup.title.get_text())
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.a)
# print(soup.find_all('a'))
print(soup.find(id='link3'))

# list = soup.findAll('a')
# for item in list:
#     print(item['id'])
































