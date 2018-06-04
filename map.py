import random, math

number= range(1,100)

num= random.sample(number,2)

num.sort()

print (num)

a = map(lambda x: math.pow(x,1/2), range(num[0],num[1]))

a = list(a)

# print (a)

b= filter(lambda x : int(x)== x, list(a))

b=list(b)

print (len(b), b)