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
We want to return an array such that 
indices show the number of days until a warmer temperature 

We can traverse the array and see if the previous days temp 
was lower than current day 

To look at the previous days temp
We can use a stack! 

Our stack will contain the pair [temp, index]

Using our stack, 
WHILE 
our current temperature is greater than previous days 
we'll need to add a one AT THE INDEX of the PREVIOUS day
and we pop previous from our stack 

At the index of the previous day
i.e stackIdx

we'll place the difference in idxs
answer[stackIdx] = (idx - stackIdx)

finally we append to our stack
[temp, idx]

return ans 

"""

class Solution(object):
    def dailyTemperatures(self, temperatures):

        ans = [0] * len(temperatures)

        stack = []

        for idx, temp in enumerate(temperatures):

            # while our stack is not empty
            # and our current temperature is greater than previous days
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()

                # at stackIdx
                # put respective difference
                ans[stackIdx] = (idx - stackIdx)

            # append
            stack.append([temp, idx])

        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    print(Solution().dailyTemperatures(temperatures))

