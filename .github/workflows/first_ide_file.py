
"""
name = "Alex"

name = "Alex li"
print(name)

NAME = "Alex"

AGE_OF_OLDBOY = 56
"""

"""
select_red_ball = []
while True:
    n = int(input('请输入你要选择的红色球(1-32)：'))
    if 0 < n < 33:
        if n not in select_red_ball:
            select_red_ball.append(n)
        else:
            print('number %d is already exist in red ball list' % n)
    else:
        print('only can select n between 1-32')
    if len(select_red_ball) == 6:
        break
select_red_ball.sort()
select_blue_ball = []
while True:
    n = int(input('请输入你要选择的蓝色球(1-32)：'))
    if 0 < n < 17:
        if n not in select_blue_ball:
            select_blue_ball.append(n)
        else:
            print('number %d is already exist in blue ball list' % n)
    else:
        print('only can select n between 1-16')
    if len(select_blue_ball) == 2:
        break
select_blue_ball.sort()
print('red ball %d' % select_red_ball)
print('blue ball %d' % select_blue_ball)
"""
"""
while True:
    select = input("请输入高考分数:")
    select = int(select)
    if select>=0 and select< 60:
        print("成绩不及格,补考")
    elif select>=60 and select< 70:
        print("成绩为D")
    elif select>=70 and select< 80:
        print("成绩为C")
    elif select>=80 and select< 90:
        print("成绩为B")
    elif select>=90 and select< 100:
        print("我太优秀了")
    break
"""


"""
name = "小明"
age = 22
height = 160
age = 88
address ="北京昌平沙河"
print(name)
print(age)
print(address)

# 鸵峰体的变量定义方式:

AgeOfoOdboy = 56
NumberOfStudents = 80

print(AgeOfoOdboy+NumberOfStudents)

# 下划线定义
age_of_oldboy = 56
number_of_students = 80
print(age_of_oldboy*number_of_students)

# 常量定义方式

AGE_OF_OLDBOY = 56

"""
"""
a = 2
b = 5
if a == b:

    print('要带')
else:
    print('不用带')
"""
"""
age1 = 18
age2 = age1
age1 = 12
age3 = age2
print(age1,age2,age3)
"""

name = input("输入你的名字:")
age = input("输入你的年龄:")
height = input("输入你的身高:")
question = input("你是不是全身都黑:")

msg = '''
-----------------Perdonal Info-------------
Name        : %s
Age         : %d
Heighi      : %s
Answer      : %s
----------------End------------------------
''' % (name,age,height,question)

print(msg)

if question == "Y" or question=="y":
    print("我不信,让我看看。。。。")























