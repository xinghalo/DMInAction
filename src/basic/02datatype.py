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
str1 = 'runjob'
print(str1)
print(str1[0:-1])
print(str1[0])
print(str1[2:5])
print(str1[2:])
print(str1*2)
print(str1+"test")
print('Run\noob')
print(r"Run\noob")
word = 'Python'
print(word[0],word[5])
print(word[-1],word[-6])
# python不能用下标更改字符串
# * 表示重复，+表示连接
# 左边从0开始，右边从-1开始
# 字符串不能改变

list1 = ['a',789,2.23,'run',70.2]
tinylist = [123,'run']
print(list1)
print(list1[0])
print(list1[1:3])
print(list1[2:])
print(tinylist*2)
print(list1+tinylist)
a = [1,2,3,4,5,6]
a[0] = 9
a[2:5] = [13,14,15]
print(a)
a[2:5] = [] # 删除
print(a)

tuple1 = ('1',786,2.23,'run',70)
tinytuple = (123,'run')
print(tuple1)
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[2:])
print(tinytuple * 2)
print(tuple1+tinytuple)
# 不可以修改元组

student = {'tom','jim','mary'}
print(student)
if('tom' in student):
	print("zai")
else:
	print("buzai")

a = set('abcd')
b = set('efg')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)


dict1 = {}
dict1['one'] = "1"
dict1[2] = "2"
tinydict = {'name':'tom','code':2}
print(dict1['one'])
# print(dict[1])
print(dict1[2])
print(dict1)
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

print(dict([('r',1),('b',2)]))
print({x:x**2 for x in (2,4,6)})
print(dict(r=1,b=2,c=4))

# 其他的方法
print(int(2.3))
print(float(2))
print(complex(2))
print(complex(2,1))
print(str(2.2))
print(repr(1+2))# ?
print(eval('1+2'))
print(tuple([1,2,3]))
print(list({1,1,2,3}))
print(set([1,2,3,3,3]))
print(dict([(1,2)]))
print(frozenset([1,2,3])) # 不可以变
frozenset1 = frozenset([1,2,3])
# frozenset1[0] = 2
print(frozenset1)
print(chr(65))
# print(unichr(65))
print(ord('A'))
print(hex(32))
print(oct(10))