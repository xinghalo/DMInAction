list1 = [1,2,3,4]
it = iter(list1)
print(next(it))
print(next(it))

for x in it:
	print(x,end=" ")