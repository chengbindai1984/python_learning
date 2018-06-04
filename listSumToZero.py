import random

def listSum(number):
    import random
    list= []
    sum = 0

    for i in range (1, number):
        n = random.randint(-9999,9999)
        list.append(n)
        #  print (list)
        sum = sum + n

    balanceVale = -sum
    list.append(balanceVale)
    # print (sum)
    print (list)

inputNum = random.randint(1, 9)

print ('Input number is '+str(inputNum))

listSum(inputNum)