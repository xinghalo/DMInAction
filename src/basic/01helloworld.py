#!/usr/bin/python3
# 指定了用哪一个Python
# -*- coding: utf-8 -*-
print("Hello,world!")# 注释
# 注释1
# 注释2

# 缩进很重要
if True:
	print("True")
else:
	print("False")
print("False2")

# 过长的表达式可以通过 \ 换行表示
item_1 = item_2 = item_3 = 1
total = item_1+\
		item_2+\
		item_3

print(total)

# 数据类型
# 整数、长整数、浮点数、复数

# 字符串
str1 = '1a'
str2 = "1a"
str3 = ''' aaa

aaa
'''
str4 = """
fdsafda \r
fdas
"""
str5 = r"hello \r heihei"
print(str1,str2,str3,str4,str5)

# 用户输入
# input("\n\n 按下 enter 后退出：")

# 多行
import sys; x = 'runjob'; sys.stdout.write(x+'\n')

# 多语句
a = 6
if a>0:
	print("0")
elif a>5:
	print("5")
else:
	print("-1")

# 输出
x="a"
y="b"
# 换行
print(x)
print(y)

print("--------")
# 不换行
print(x,end=" ")
print(y,end=" ")
print()

# import xxx 导入整个模块
# from xxx import yyy 导入xxx模块的yyy函数
# from xxx import y1,y2,y3 导入xxx模块的多个函数
# from xxx import * 导入模块的所有函数
import sys
print(sys.path)
from sys import path
print(path)