import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
import random


# line = 'pashazera'
# rex = '^p.*'
# if re.match(rex,line):
#     print('yes')

# def foo():
#     print("starting...")
#     while True:
#         res = yield random.randint(1,10)
#         res = 0
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))
# print(next(g))

def print_rex(line, rex):

    if re.match(rex, line):
        print(line + '  正则表达式匹配结果为  yes')
    else:
        print(line + '  正则表达式匹配结果为  no')


rex_name = '^[\\u4E00-\\u9FA5][\\u4E00-\\u9FA5|·]*[\\u4E00-\\u9FA5]$|(^$)'
shop_uuid = '^[0-9]{18,20}$|^$'
national_code = '^[0-9]{13}$'

longitude = '(^-?(0(\\.\\d{10})?|([1-9](\\d)?)(\\.\\d{10})?|1[0-7]\\d{1}(\\.\\d{10})?|180\\.0{10})$)|^[ \\t]*$'
latitude = '(^[\\-\\+]?((0|([1-8]\\d?))(\\.\\d{10})?|90(\\.0{10})?)$)|^[ \\t]*$'
prvn_code = '^[1-9]{1}[0-9]{3}[0]{2}$|(^$)'
city_code = '^[1-9]{1}[0-9]{5}$|(^$)'
mobile = '^((13[0-9])|(14[0-9])|(15[0-9])|(17[0-9])|(18[0-9]))\\d{8}$'

print_rex('-77.0364640000', longitude)

operating_state = '^[0|1]$'

uid = '^[0-9]*$|^$'
emp_type = '^[0|1|2|3]$'
pro_barstatus = '^0[1|2|3]$|^$'
print_rex('3', pro_barstatus)

rex_date = '^[1-9]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\\s+(20|21|22|23|[0-1]\\d):[0-5]\\d:[0-5]\\d$'
date = '2019-01-01 08:54:28'
reg = '^[1-9]{1}\\d{0,}(\\.\\d+)?$'
freg = '^[1-9]{1}\\d+(\\.?)\\d+$'
print_rex(date, rex_date)
print(len('http://manager.openmig.cn:8080/mig-manager/fileService/'))

n = '^[细支烟|标准烟]$'
m = '^细支烟$|^标准烟$|^粗支烟$|^中支烟$'
print_rex('标准烟', n)

# 空行^\[ \t]*$
no_col = '^[ \\t]*$'
no_col1 = '^[ ]{0,}$'
print_rex('            ', no_col1)

x = '^[1-9]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$'
print_rex('2019-02-01', x)
a = '^[1-9]\\d{3}(,[1-9]\\d{3}){0,}$'
print_rex('2018', a)
money = '^[1-9]\\d{0,}$|^0$'
print_rex('1', money)
s = '^(EVT-22-ACT-)\\d{4}(-)\\d{10}$'
print_rex('EVT-22-ACT-1350-1545108524', s)

p = '2019-01-01'

s = '^$'
print_rex('    ', s)
b = '^.{0,}$|^[ \\t]*$'
print_rex('(二毛蔬菜水果超市)张店二毛超市', b)
print('202cb962ac59075b964b07152d234b70')
