# 类型自动推断
counter = 100
miles 	= 1000.0
name 	= 'runjob'

print(counter)
print(miles)
print(name)

# 多个变量同时赋值
a = b = c = 1
print(a,b,c)
a,b,c = 1,2,'hello'
print(a,b,c)

'''
标准的数据类型：
Number,String,List,Tuple,Sets,Dictionary

Number:
int,float,bool,complex
'''
a,b,c,d=20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

# 类型判断
a = 111
print(isinstance(a,int))

class A:
	pass
class B(A):
	pass
print(isinstance(A(),A))
print(type(A()) == A)
print(isinstance(B(),A))
print(type(B()) == A) #False

v1 = 1
v2 = 2
# del v2
# print(v2) 会报错

# 数值运算
print(5+4)
print(5-4)
print(5*4)
print(5/4) # 小数
print(5//4) # 整数
print(5%4)
print(5**4)

# 字符串
str = 'runjob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+"test")