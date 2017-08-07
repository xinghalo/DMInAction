d = {'Tom':21,'Jery':25}
d1 = {'a':'b'}

print(d['Tom'])

# 修改
d['Tom'] = 22
print(d)

# 删除
del d['Jery']
print(d)

d1.clear()
print(d1)

print(len(d))
print(str(d))
print(type(d))

# 复制
d2 = d.copy()
print(d2)

# print(d2.fromkeys())
print(d2.get('Tom'))
d2['haha'] = 23

# 循环
for key in d2: print(key)

# 获得每个元素
print(d2.items())

# 获得字典的key和value
print(d2.keys())
print(d2.values())

# 更新Seq中的元素
d2.update({'Tom':26})
print(d2)

# 弹出一个元素
print(d2.pop('Tom'))
print(d2)

d2['other'] = 30
print(d2.popitem()) # 随机返回一个
print(d2)