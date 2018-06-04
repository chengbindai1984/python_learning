
'''
一般的递归
'''
def fib(i):
    if i < 2: 
        return 1
    else:
        return fib(i-1)+fib(i-2)

for i in range (1,8):
    fib(i)

'''
添加了缓存装饰器的递归
需要理解装饰器的用法
'''

from functools import wraps

def memo(func):
    cache={}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap

@memo
def fib(i):
    if i<2: return 1
    return fib(i-1)+fib(i-2)

for i in range (1,80):
    fib(i)

’‘’
迭代方法（动态规划）
‘’‘

def fib(i):
    if i < 2: return 1
    a,b=1,1

    while i>=2:
        c=a+b
        a=b
        b=c
        i=i-1
    return c

fib(8000)

def cnk(n,k):
    if k==0: return 1 #the order of `if` should not change!!!
    if n==0: return 0
    return cnk(n-1,k)+cnk(n-1,k-1)

cnk(99,5)

from functools import wraps

def memo(func):
    cache={}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap

@memo
def cnk(n,k):
    if k==0: return 1 #the order of `if` should not change!!!
    if n==0: return 0
    return cnk(n-1,k)+cnk(n-1,k-1)

cnk(99,55)

def cnk (n,k):
    c=defaultdict(int)
    for row in range(1,n+1):
        c[row,0]=1
        for col in range(1,k+1):
            c[row,col]=c[row-1,col-1]+c[row-1,col]
    return c[n,k]
cnk(99,55)