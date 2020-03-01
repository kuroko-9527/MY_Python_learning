# 打印0-100的所有奇数
i = [i for i in range(100) if i % 2 != 0]
print(i)

# 长阶梯，每步上两阶，最后剩余1阶，每步3阶 剩余2阶，每步5阶 剩余4阶 每步6阶 剩余5阶 只有每步七阶 刚好1阶不剩
# n%2 = 1
# n%3 = 2
# n%5 = 4
# n%6 = 5
# n%7 = 0
# 首先n需要＞7，
# 笨方法1.0
x = 10000
list1 = []
for n in range(7, x):
    if n % 2 == 1 and n % 3 == 2 and n % 5 == 4 and n % 6 == 5 and n % 7 == 0:
        list1.append(n)
print(list1)

# 方法 2.0 找到第一个数就返回
n = 7
while True:
    if n % 2 == 1 and n % 3 == 2 and n % 5 == 4 and n % 6 == 5 and n % 7 == 0:
        print(n)
        break
    else:
        n += 1
# 变量转换
x = 1
y = 2
z = 3
x, y, z = z, x, y
print("x={0},y={1},Z={2}".format(x, y, z))

# 成员资格运算符 in 的用法
# for i in xxx：
# 还可以用组排判断语句
ls = [1, 2, 3, 4, 99]
if 100 in ls:
    print("True")
else:
    print("Flase")

# range 函数的用法
range(0, 100, 2)  # 的意思是 [0,100),左包含 右不包含，2是步长

# 代码改进
# i= 0
# string = "iloveTuling"
# while i < len("string"） # 不要再循环中调度哈数
#    print(i)
#    i += 1
# 优化后应采用判断语句
string = "i love June very very much"
i = len(string)
list1 = []
for x in range(0, i):
    if x == 0:
        str = string[0]
    else:
        str += string[x]
#    list1.append(string[x])
print(str)
