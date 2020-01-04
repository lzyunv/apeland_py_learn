


#today_weather = "sun_day"

# #单分支
#if today_weather == "rain_day":
# print("take your umbrella with you ")

# 双分支
# age_of_oldboy = 58
# if age_of_oldboy > 50:
#     print("Too old, time to retire..")
#     print("hahah")
# else:
#     print("还能折腾几年!")

#
# age = 35
#
# if age < 12:
#     print("you are child")
# elif age < 18:
#     print("you are teenager")
# elif age < 30:
#     print("you are young man")
# else:
#     print("your are oil middle-age man")
#
# import random
#
# n = random.randint(0,10)
#
# user_guess = int(input("Input your guess:"))
#
# if user_guess > n :
#     print("try smaller...")
# elif user_guess < n :
#     print("try bigger....")
# else:
#     print("bingo, you got it ....")
#
#
# print(n)



# count = 0
#
# while count < 100:
#
#     if count % 2 == 0:
#         print("我想让你得到我。。。。", count)
#     count += 1


# import random
#
# n = random.randint(0,10)
#
# count = 0
# while count < 5:
#     user_guess = int(input("Input your guess:"))
#
#     if user_guess > n :
#         print("try smaller...")
#     elif user_guess < n :
#         print("try bigger....")
#     else:
#         print("bingo, you got it ....")
#         break # 中止循环
#
#     count +=1
#
# print(n)
#
# count = 0
# while count < 100:
#     count += 1
#     # if count > 10 and count < 20:
#     #     continue #
#     if count == 50:
#         break
#     print(count)
# else: #当循环正常结束时，执行, 被break中止时，则不执行
#     print('sdfsfdsf')

#while True:
#    print("你是风儿我是沙，缠缠绵绵到天涯....")
'''
name = input("What is your name?")
age = input("How old are you ？")
hometown = input("Where is your hometown ？")
print("Hello",name,"your are",age,"years old, you came from",hometown
      )

'''

while True:
    age = input("请输入你女朋友胸围:")
    age = float(age)

    if age >=0 and age<60:
        print("你女朋友为E罩杯胸围")

    elif age >=60 and age<70:
        print("你女朋友为D罩杯的胸围")

    elif age>=70 and age<80:22
        print("你女朋友为C罩杯的胸围")
    elif age>=80 and age<90:
        print("你女朋友为B罩杯的胸围")

    elif age>=90 and age<100:
        print("你女朋友为A罩杯的胸围")
        break


"""
import  random
n = random.randint(0,10)

count = 0
while  count < 5:
        user_guess = int(input("Input your guess:"))
        if user_guess > n :
            print("try smaller....")
        elif user_guess < n :
            print("try bigger....")
        else:
            print("bingo, you got it .....")
            break


        count += 1
        print(n)

"""
"""
count = 0

while count < 100:
    if count % 2 == 0:
        print("我想让你得到我。。。",count)

    count +=  1
"""


"""
count = 0
while count < 100:
    count += 1
    if count > 10 and  count < 20:
        continue
        break

    print(count)
else:
    print("sdfsfdsf")




#while True:
 #  print("你是风儿我是沙，缠缠绵绵到天涯....")
"""






