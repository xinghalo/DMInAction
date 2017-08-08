# var1 = 100
# if var1:
# 	print("1 - if : true")
# 	print(var1)

# var2 = 0
# if var2:
# 	print("2 - if : true")
# 	print(var2)
# print('goodbye')
age = int(input("输入"))
print("")
if age < 0 :
	print("are you kidding!")
elif age == 1:
	print("相当于人14岁")
elif age == 2:
	print("相当于人22岁")
elif age > 2:
	human = 22 + (age-2)*5
	print("对应人类年龄：",human)

input("点击 enter 退出")