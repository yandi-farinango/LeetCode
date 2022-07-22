"""
Given an integer array nums and an integer k,
return the k most frequent elements.

You may return the answer in any order.
"""


"""
We'll use freqMap 
to map nums:freq

and bucket
to sort numbers into freq "buckets"

we can create an empty result variable
to hold our final result 

we iterate through numbers within the respective buckets,
&&append to result 
return result 
"""

nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2


freqMap = {}
bucket = [[] for i in range(len(nums) + 1)]

for n in nums:
    freqMap[n] = 1 + freqMap.get(n, 0)

for number, count in freqMap.items():
    bucket[count].append(number)

res = []

for index in range(len(bucket) - 1, -1, -1):
    for numbers in bucket[index]:
        res.append(numbers)
        if len(res) == k:
            print(res)
