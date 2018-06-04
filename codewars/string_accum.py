

def accum(inputStr):
    outputList = []
    count = 0
    for v in inputStr:
        initialValue = v
        listLen = count +1
        tempList = [initialValue]*listLen
        # print (tempList)
        tempString= ''.join(tempList)
        tempString= tempString.capitalize()
        # print (tempString)
        outputList.append(tempString)
        count = count+1
        # print (outputList)
    outputString = '-'.join(outputList)
    return outputString


# 利用enumerate()简化代码

def accum(inputStr):
    outputList = []
    for i,v in enumerate(inputStr,1):
        tempList = [v]*i
        tempString= ''.join(tempList)
        tempString= tempString.capitalize()
        outputList.append(tempString)
    outputString = '-'.join(outputList)
    return outputString

# 考虑直接字符处理不用list

#未完成

def accum(inputStr):
    outputList = []
    # count = 0
    for i,v in enumerate(inputStr,1):
        tempString = v*i
        print (tempString)
        tempString= tempString.capitalize()
        print (tempString)
        outputString = '-'.join(tempString)
    return outputString


# Best One

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))