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

print('我现在测试从GitHub上同步本地代码')