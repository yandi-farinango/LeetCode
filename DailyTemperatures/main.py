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
We'll need an answer array of len(temperature)

We'll be traversing the array 
and looking to see if the previous days temperature 
was lower that current temp 

We can use a stack to look at the previous days temperature 
If it is less than current, 
We can add a 1 to our ans array 
and pop from the top of our stack 

When the current temp
is not less than previous 
We will be appending current temp to our stack 

*** If values are equal, we'll also append to our stack 

We will essentially be forming a MONOTONIC DECREASING STACK 

"""

class Solution(object):
    def dailyTemperatures(self, temperatures):

        # ans stack of len(temperatures) w/ default values of 0
        answer = [0] * len(temperatures)

        # stack will be containing pair [temp, index]
        stack = []

        # we want to enumerate temperatures
        for idx, temp in enumerate(temperatures):

            # while our stack is not empty
            # and current temp > temp at the top of our stack
            while stack and temp > stack[-1][0]:
                # well pop from the top of our stack
                stackTemp, stackIdx = stack.pop()

                # at the respective index,
                # we'll add the difference in idxs
                answer[stackIdx] = (idx - stackIdx)

            # and we finally want to append [temp, index] to our stack
            stack.append([temp, idx])
        return answer


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    print(Solution().dailyTemperatures(temperatures))

