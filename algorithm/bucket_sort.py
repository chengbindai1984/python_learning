
import random

import time

max_range = 10000
number=5000
nums=random.sample(range(1,max_range),number)


start = time.clock()


bucket = [-1]*max_range
ans=[]
for i in nums:
    bucket[i]=i

for j in bucket:
    if j != -1:
        ans.append(j)

# ans


end = time.clock()
print('Running time: %s Seconds'%(end-start))


random.shuffle(nums)
start = time.clock()

nums.sort()

end = time.clock()
print('Running time: %s Seconds'%(end-start))
