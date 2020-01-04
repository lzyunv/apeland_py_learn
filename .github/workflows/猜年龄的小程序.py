

import random

n = random.randint(0,10)

count = 0
while count < 3:
    user_gess = int(input("你猜我是你老婆还是情人还是女朋友:"))

    if user_gess > n :
        print("女朋友")
    elif user_gess < n :
        print("你情人")
    else:
        print("我的老婆")
        break
    count +=1





"""
count = 0

while count < 100:

    if count % 2 == 0:
        print("我想让你得到我。。。。",count)

    count += 1
"""
"""
count = 0
age = 33
while count < 3:
    count += 1
    age_input = int(input("请输入您猜的年龄-->:"))
    if age_input == age:
        print("恭喜您，猜对了")
        break
    elif age_input > age:
        print("您猜的年龄大于实际年龄，请下次往小一点猜")
    else:
        print("您猜的年龄小于实际年龄，请下次往大一点猜")
    if count == 3:
        choice = input("连续3次猜错,是否继续，y/n: ")
        if choice == "Y" or choice == "y":
            count = 0
        elif choice == "N" or choice == "n":
            break
        else:
            print("你输入的有误，程序结束")
"""






















