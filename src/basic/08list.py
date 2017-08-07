list1 = ['Google','Runoob',1997,2000]
list2 = [1,2,3,4,5,6,7]

print(list1[0])
print(list2[1:5])

# 更新
list1[1] = 'hello'
print(list1)

# 删除
del list1[1]
print(list1)

print(len(list1))
print([1,2,3]+[4,5,6])
print(['hehe!']*4)
print(3 in [1,2,3])
for x in [1,2,3]: print(x,end=" ")

# 嵌套
a = ['a','b','c']
n = [1,2,3]
x = [a,n]

print(x)
print(x[0])
print(x[0][1])

# 其他的方法
print(len(list2))
print(max(list2))
print(min(list2))
print(list(list2))

list2.append(3)
print(list2) # 追加元素
print(list2.count(1)) # 针对某个元素计算count
list2.extend(list1) # 拼接两个列表
print(list2) 
print(list2.index(3)) # 找出元素对应的下标
list2.insert(1,'world')
print(list2)
print(list2.pop())
print(list2)
list2.remove('Google')
print(list2)
list2.reverse()
print(list2)
list3 = list2.copy()
print(list3)
list2.clear()
print(list2)
list3.remove('world')
list3.sort(key = lambda x:(-x,x)) #自定义逆序
list3.sort(key = lambda x:(x,x)) #自定义顺序
print(list3)