# 水仙花数
# 求100-999 的所有水仙花数  abc = a^3+b^3+c^3


for i in range(100, 1000):
    a = int(i / 100)
    b = int(i / 10 % 10)
    c = int(i % 10)
    h = a ** 3 + b ** 3 + c ** 3  # 不是使用x^n的方法表示 折腾一下午
    if h == i:
        print(i)

# 三色球问题
# 红球 = 3 ，黄球 =3 ，蓝球 = 6， 从上面取8个球，编程计算摸出球的各种颜色搭配
i = 1
for r in range(0, 4):
    for y in range(0, 4):
        for b in range(0, 7):
            if r + y + b == 8:
                i += 1
                print("颜色搭配方法{0}:红色{1},黄色{2},蓝色{3}".format(i, r, y, b))
