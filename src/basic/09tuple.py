tup1 = ('Google','Runoob',1997,2000)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d"

# 空的tupe
tup4 = ()
print(tup4)

tup4 = (5)
print(type(tup4))
tup4 = (5,)
print(type(tup4))

print(tup1[0:])
print(tup1[2:3])

# 修改
#TypeError: 'tuple' object does not support 
# tup1[1] = 'hello'

#删除
# TypeError: 'tuple' object doesn't support item deletion
# del tup1[1]

# 常用的方法
# len max min tuple