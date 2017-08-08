# 栈
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

# 队列
from collections import deque
queue = deque([2,3,4,5])
queue.append(6)
queue.append(7)
print(queue.popleft())
print(queue.popleft())
print(queue)

# 列表推导式
vec = [2,4,6]
print([3*x for x in vec])
print([[x,x**2] for x in vec])

freshfruit = ['   banana','   loganberry ','passion   ']
print([weapon.strip() for weapon in freshfruit])

print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])

vec1 = [2,4,6]
vec2 = [4,3,-9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
print([str(round(355/113,i)) for i in range(1,6)])

# dict 遍历
knights = {'a':1,'b':2,'c':3}
for k,v in knights.items():
	print(k,v)