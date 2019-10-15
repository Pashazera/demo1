"""
    Author: Pashazera
    Time  : 2019/10/14 14:18
    File  : 批量 更改文件名.py
    describe : 批量修改文件名
"""


import os
import re
import sys


def renameall():
    fileList = os.listdir(r"E:\win")  # 待修改文件夹
    print("修改前：" + str(fileList))  # 输出文件夹中包含的文件
    currentpath = os.getcwd()  # 得到进程当前工作目录
    os.chdir(r"E:\win")  # 将当前工作目录修改为待修改文件夹的位置
    num = 1  # 名称变量
    for fileName in fileList:  # 遍历文件夹中所有文件
        # pat = ".+\.(jpg|png|gif)"  # 匹配文件名正则表达式
        # pattern = re.findall(pat, fileName)  # 进行匹配
        # os.rename(fileName, (str(num) + '.' + pattern[0]))  # 文件重新命名
        os.rename(fileName,fileName + '.jpg')
        num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(currentpath)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    print("修改后：" + str(os.listdir(r"E:\win")))  # 输出修改后文件夹中包含的文件



renameall()
