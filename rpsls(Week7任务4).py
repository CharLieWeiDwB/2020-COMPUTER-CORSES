#coding:gbk
"""
项目：Rock-paper-scissors-lizard-Spock
程序目标：利用python完成RPSLS游戏
作者：魏彬航
日期：2020年11月24日
"""

import random

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":  # 使用if/elif/else语句将各游戏对象对应到不同的整数
        number=0
    elif name=="史波克":
        number=1
    elif name=="纸":
        number=2
    elif name=="蜥蜴":
        number=3
    elif name=="剪刀":
        number=4
    return number
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:   # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
        name="石头"
    elif number==1:
        name="史波克"
    elif number==2:
        name="纸"
    elif number==3:
        name="蜥蜴"
    elif number==4:
        name="剪刀"
    return name
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    if player_choice in ("石头","剪刀","史波克","纸","蜥蜴","剪刀"):
        print("-------- ")  # 输出"-------- "进行分割
        player_choice_number = name_to_number(player_choice)
                                              # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
        comp_number = random.randrange(0, 5)  # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
        comp_choice = number_to_name(comp_number)   # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
        print("您的选择为：" + player_choice)  # 在屏幕上显示计算机选择的随机对象
        print("计算机的选择为：" + comp_choice)
        competition = (player_choice_number - comp_number) % 5
        if competition == 1 or competition == 2:  # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
            print("您赢了！")
        elif competition == 3 or competition == 4:
            print("计算机赢了！")
        else:
            print("您和计算机出的一样呢")
    else:print("Error: No Correct Name")  # 用户的选择不是石头/剪刀/布/蜥蜴/史波克中的任意一个，输入错误
    return


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()  # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量choice_name
rpsls(choice_name)  # 用自定义rpsls函数进行游戏


