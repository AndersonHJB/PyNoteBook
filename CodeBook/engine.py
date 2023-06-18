# -*- coding: utf-8 -*-
# @Time    : 2023/6/18 10:44
# @Author  : AI悦创
# @FileName: engine.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from CodeBook.variable import variable


def search(string: str):
    if string.isalpha():
        variable.show()
    else:
        print("Error")
