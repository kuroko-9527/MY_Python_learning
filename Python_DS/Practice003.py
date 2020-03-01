# 设计一个验证用户的密码程序，用户只有三次机会输入错误，不过用户输入的内容包括""则不再计算内

times = 3
rightpassword = "12345"
while times:
    password = input("请输入密码:")
    if r'*' in password:
        print("您输入的密码包含*,不计算输入次数")
    elif password != rightpassword:
        print("输入错误")
        times -= 1
        print("当前剩余输入次数为{0}".format(times))
    else:
        print("您的密码输入正确")
        break
