import sys

print('params:')
for i in sys.argv:
	print(i)

# 模块搜索的路径
print(sys.path)

# 第一种引用方式
# from xxx import yyy 
# yyy()

# 第二种引用方式
# from xxx import *
# yyy()

if __name__ == '__main__':
	print('run this')
else:
	print('other not run')

print(sys)