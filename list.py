from __future__ import print_function


def list_to_string(mylist):
    import copy
    print (mylist)
    templist=copy.copy(mylist)
    templist[len(templist)-1]= ' and  '+templist[len(templist)-1]
    print (mylist)
    print (templist)
    for i in range(len(templist)):
        print (templist[i], end=', ')
    print ('\n')

# 加入用户输入模块
spam = ['1', '2', '3', '4', '99']


list_to_string(spam)
