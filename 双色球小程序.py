"""
count = 0
while count < 10:
    count += 1
    if count <= 5:
        print(count * " * ")
    else:
        print((10 - count) * " * ")
"""

"""
count = 0
import  random
age = random.randint (1,40)

while count < 3:
    count += 1
    age_input = int(input("请输入您猜的年龄-->:"))
    if age_input == age:
        print("恭喜你，答对了")
        break
    elif age_input > age:
        print("您猜的年龄大于实际年龄，请下次往小一点猜")
    else:
        print("您猜的年龄小于实际年龄，请下次往大一点猜")
    print(age)
    if  count == 3:
        choice = input("连续3次猜错,是否继续，y/n:")
        if choice == "Y" or choice == "y":
            count = 0
        elif choice == "N" or choice == "n":
            break
        else:
            print("你输入的有误，程序结束")
    """

"""
import random

# red_num_chaos 是采集红色球的数字，
# 集合的目的是不用判断随机数字是否重叠
red_num_chaos = set()
while True:
    chaos_num = int(random.random() * 34)  # random.random()返回随机生成的一个实数，它在[0,1)范围内，所以要想得到33，必须乘以34
    if chaos_num == 0:
        continue
    else:
        red_num_chaos.add(chaos_num)  # add()方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作
    if len(red_num_chaos) == 6:
        break

# 将集合进行排序
red_num = sorted(red_num_chaos)
# 将集合转为列表的形式，方便向该数字中增加蓝色数值，
# 集合中不能出现重复的，而1位蓝色数字有可能会与6位红色相等
double_ball = list(red_num)

# 生成一个不为0的1～16的蓝色球数字
while True:
    blue_num = int(random.random() * 17)
    if blue_num != 0:
        break

# 　组合成双色球
double_ball.append(blue_num)
print(double_ball)

"""

redlist = []
bluelist = []

count = 0
count2 = 0                                                                     

while count < 6:
    red1 = input("-------输入你要选的红色球---------")
    if not  red1.isdigit():
        print("输入数字")
        # red1 = int(red1)
    elif red1 in redlist or int(red1) > 32 or red1 == 0:
        print("红色球可选择范围1-32 ")
        print("红色球存在or超出可选范围 ")
        continue

    else:

        redlist.append(red1)
        count += 1


while count2 < 2:
    blue1 = input("~~~~~~~输入你要选的蓝色球~~~~~~~~")
    if not  blue1.isdigit():
        print("输入数字")
    elif blue1 in bluelist or int(blue1) > 16 or blue1 == 0:
        print("蓝色球可选范围1-16 ")
        print("蓝色球已经存在or超出可选范围")
        continue
    else:
        bluelist.append(blue1)
        count2 += 1

redlist.sort()
bluelist.sort()

print('你选择的红球为:',redlist)
print('你选择的篮球为:',bluelist)
































