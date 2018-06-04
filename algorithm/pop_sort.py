


import random

import time

max_range = 10000
number=5000
nums=random.sample(range(1,max_range),number)

start = time.clock()


for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j] > nums[j+1]:
            t=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=t

end = time.clock()
print('Running time: %s Seconds'%(end-start))

