# 简单图形打印

# 打印以下形状
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
for i in range(5):
    print(" *" * 5)

"""
* * * * *
*       *
*       *
*       *
* * * * *
"""
for i in range(5):
    if i == 0 or i == 4:
        print(" *" * 5)
    else:
        print(" *       *")

"""
* 
* *
* * * 
* * * *
* * * * *
"""

for i in range(1, 6):
    print(" *" * i)

"""
* 
* *
*   * 
*     *
* * * * *
"""
print("-" * 50)
n = 5
for i in range(1, n):
    if i <= 1 or i == n - 1:
        print(" *" * i)
    else:
        print(" *" + r"  " * (i - 2) + " *")

print("+" * 50)
"""
* * * * *
* * * *
* * * 
* * 
* 
"""
# 扩展知识 range反序  方法1
n = 6
list1 = [i for i in range(6, -1, -1)]
print(list1)
# 扩展知识 range反序 方法2
n = 6
list2 = [i for i in reversed(range(n))]
print(list2)

for i in reversed(range(1, 6)):
    print(" *" * i)

# 打印空倒三角
n = 6
for i in reversed(range(1, n)):
    if i == 1 or i == n - 1:
        print(" *" * i)
    else:
        print(" *" + r"  " * (i - 2) + " *")

# continue 语句的使用
n = 6
for i in range(n):
    for j in range(n - i):
        if i == 0:
            print(" *", end="")
            continue  # 程序设计思路，跳过本次for循环。
        if j == 0 or j == n - i - 1:  # 首尾 打印* 剩余打印空格 程序的设计思想很重要~
            print(" *", end="")
        else:
            print("  ", end="")
    print("")

# 打印正三角形  (98line ""中空格数量影响着结果，画图能够理解）
n = 6
for i in range(n):
    for j in range(6 - i):
        print(" ", end="")
    for m in range(i + 1):
        print("* ", end="")
    print("")
# 打印整空心正三角形
# 多绕几遍~
n = 6
for i in range(1, n):
    for k in range(1, n - i):
        print(" ", end="")
    for j in range(n - i, n):
        if i == n - 1 or j == n - i or j == n - 1:
            print(" *", end="")
        else:
            print("  ", end="")
    print()
