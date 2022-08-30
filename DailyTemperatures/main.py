"""
Given an array of ints, temperatures
representing daily temperatures

return an array, answer,
such that answer[i]
is the number of days
you have to wait,
after the ith day,
to get a warmer temperature

If there is no future day
for which this is possible
keep answer[i] == 0
"""

"""
Given array, temperatures
    index = day
    val = temperature 

We want to return an array, ans 

such that ans[i]
is the number of days
until a higher temperature 

len(ans) will be = len(temperatures)

We can start by creating ans[0] * len(temperatures)


ans[i] should be the number of days until a higher temperature


We can use a stack 
where we will be appending [temp, index]


We can traverse temperatures 
using 
for index, temp in enumerate(temperatures)

while we have values in our stack, 
we can compare the previous days temp to our current days temp 
previous days can be found in stack[-1][0]

while current day temp > stack [-1][0]

we'll keep popping
stackTemp, stackIndex from our stack 
until we get to a temp 

and at the respective index 
ans[index] = current index - stackIndex
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):

        ans = [0] * len(temperatures)

        # we'll be appending [stackTemp, stackIndex]
        stack = []

        for index, temp in enumerate(temperatures):
            # while stack and our previous day's temp < current temp
            while stack and stack[-1][0] < temp:
                stackTemp, stackIndex = stack.pop()

                ans[stackIndex] = index - stackIndex

            stack.append([temp, index])

        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    print(Solution().dailyTemperatures(temperatures))

