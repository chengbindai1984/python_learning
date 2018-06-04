
 

import random

import time
# 生成整数序列

number=5000
nums=random.sample(range(1,10000),number)

if nums=[]:
    return []

nums.sort()

dp = [1]*len(nums)
ind = [-1]* len(nums)

for i in range(len(nums)):
    t = 1
    for j in range(i):
        if nums[i]%nums[j] == 0 and dp[j]+ 1 >=t:
            t = dp[j]+1
            ind[i]=j
    dp[i] = t

i = dp.index(max(dp)) 

res = []
while i >= 0:
    res.append(nums[ind[i]])
    i = ind[i]

res.sort()

 '''
 以下是备份，从最小数开始筛选
 '''


 def common_multiple(base,numlist):
        answer =[]
    for i in numlist:
        if i % base == 0:
            answer.append(i)
    
    return answer

def common_multiple_r(base,numlist):
    answer =[]
    for i in numlist:
        if base % i == 0:
            answer.append(i)
    
    return answer

import random

import time
# 生成整数序列

number=5000
sample=random.sample(range(1,10000),number)


sample.sort()

'''
从最小数开始取整数集数
'''

# start = time.clock()
# 从最小整数开始，逐个进行整除处理，如果可以整除，则生成新的序列

bucket=[]

for i in sample:
    # print ("从"+str(i)+'开始')
    ans=[]
    tempList = common_multiple(i,sample)
    print (tempList)

    while len(tempList) >=1:
        tempList = common_multiple(tempList[0],tempList)
        if len(tempList) > 2:
            ans.append(tempList[0])
            tempList.remove(tempList[0])
           # print (tempList)
        elif len(tempList) == 2:
            ans.append(tempList[0])
            ans.append(tempList[1])
            tempList.remove(tempList[1])
            tempList.remove(tempList[0])
        
        elif len(tempList) == 1:
            ans.append(tempList[0])
            tempList.remove(tempList[0])
        # print (ans)

    bucket.append(ans)

out = []

for i in bucket:
    if len(i) > len(out):
        out = i

print (out)


'''
从最大数开始取整
'''

sample.sort(reverse=True)

bucket_r=[]

for i in sample:
    # print ("从"+str(i)+'开始')
    ans=[]
    tempList = common_multiple_r(i,sample)
    print (tempList)

    while len(tempList) >=1:
        tempList = common_multiple_r(tempList[0],tempList)
        if len(tempList) > 2:
            ans.append(tempList[0])
            tempList.remove(tempList[0])
           # print (tempList)
        elif len(tempList) == 2:
            ans.append(tempList[0])
            ans.append(tempList[1])
            tempList.remove(tempList[1])
            tempList.remove(tempList[0])
        
        elif len(tempList) == 1:
            ans.append(tempList[0])
            tempList.remove(tempList[0])
        # print (ans)

    bucket_r.append(ans)

out_r = []

for i in bucket_r:
    if len(i) > len(out_r):
        out_r = i

print (out_r)


if len(out) > len(out_r):  
    print (out)
else : 
    print (out_r)

# end = time.clock()
# print('Running time: %s Seconds'%(end-start))



