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

line = 'pashazera'
rex = '^p.*'
if re.match(rex,line):
    print('yes')

def foo():
    print("starting...")
    while True:
        res = yield random.randint(1,10)
        res = 0
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print(next(g))