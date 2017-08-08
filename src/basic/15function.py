def hello():
	print("hello")

hello()

def area(width,height):
	return width*height

def print_welcome(name):
	print("welcome",name)

print_welcome("xingoo")
w = 4
h = 5
print(area(4,5))
print(area(height=3,width=2))

# 变量没有类型

# 不可变类型，如a=5,a=10
# 可变类型，如a = [1,2,3]a，a[1] = 3

# 参数传递，值的传递是不可变的；列表等的传递是可变的

# 默认参数
def func1(name,age=20):
	print(name,age)

func1('tom')
func1('jery',30)

# 不定长参数
def func2(arg1,*vartuple):
	print('output:')
	print(arg1)
	for var in vartuple:
		print(var)
	return;

func2(10)
func2(10,11,12,13)

# 匿名函数
mysum = lambda arg1,arg2: arg1+arg2
print("+",mysum(10,20))
print("+",mysum(20,20))