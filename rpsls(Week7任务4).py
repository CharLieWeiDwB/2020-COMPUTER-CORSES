#coding:gbk
"""
��Ŀ��Rock-paper-scissors-lizard-Spock
����Ŀ�꣺����python���RPSLS��Ϸ
���ߣ�κ��
���ڣ�2020��11��24��
"""

import random

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":  # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
        number=0
    elif name=="ʷ����":
        number=1
    elif name=="ֽ":
        number=2
    elif name=="����":
        number=3
    elif name=="����":
        number=4
    return number
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:   # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
        name="ʯͷ"
    elif number==1:
        name="ʷ����"
    elif number==2:
        name="ֽ"
    elif number==3:
        name="����"
    elif number==4:
        name="����"
    return name
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    if player_choice in ("ʯͷ","����","ʷ����","ֽ","����","����"):
        print("-------- ")  # ���"-------- "���зָ�
        player_choice_number = name_to_number(player_choice)
                                              # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
        comp_number = random.randrange(0, 5)  # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
        comp_choice = number_to_name(comp_number)   # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
        print("����ѡ��Ϊ��" + player_choice)  # ����Ļ����ʾ�����ѡ����������
        print("�������ѡ��Ϊ��" + comp_choice)
        competition = (player_choice_number - comp_number) % 5
        if competition == 1 or competition == 2:  # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
            print("��Ӯ�ˣ�")
        elif competition == 3 or competition == 4:
            print("�����Ӯ�ˣ�")
        else:
            print("���ͼ��������һ����")
    else:print("Error: No Correct Name")  # �û���ѡ����ʯͷ/����/��/����/ʷ�����е�����һ�����������
    return


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()  # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������choice_name
rpsls(choice_name)  # ���Զ���rpsls����������Ϸ


