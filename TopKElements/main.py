nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2

freqMap = {}

# bucket = [[] for i in range(len(nums) + 1)]
bucket = [[]] * (len(nums) + 1)

for n in nums:
    freqMap[n] = 1 + freqMap.get(n, 0)

for number, count in freqMap.items():
    bucket[count].append(number)

res = []

for index in range(len(bucket) - 1, 0, -1):
    for number in bucket[index]:
        res.append(number)
        if len(res) == k:
            print(res)