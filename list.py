from __future__ import print_function


def list_to_string(list):
    list[len(list)-1]= ' and  '+list[len(list)-1]
    for i in range(len(list)):
        print (list[i], end=', ')

# 加入用户输入模块
spam = ['1', '2', '3', '4', '99']

list_to_string(spam)
