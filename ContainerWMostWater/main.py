"""
You are given
    int array, height,
    len(height) = n

There are
    n vertical lines

    drawn such that
    two endpoints
    of the ith line are
        (i, 0) and (i, height[i])

Find two lines that,
together w x-axis,
form a container

Such that container
contains the most water

Return max amount of water
a container can store

    *** Note ***
    You may NOT slant the container
"""

"""
We want to return the max volume of a container 

array, height, is given where vals are heights 
and index corresponds to x coordinate 

volume = height * width 


We can use two pointers! 

We'll start by initializing the pointers
on opposite ends of height array 

    * this maximizes our width right off the bat 
    i.e width = rightPointer - leftPointer 
    

We'll calculate container vol as 
    vol = min(height[left], height[right]) * (right - left)
        * we use min(height...) b/c
        our container CANNOT be slanted 
        
We'll have a global variable, maxVol, 
which will be continuously updated w max(vol, maxVol)


While left < right
we'll want to continuously shift the pointer
at the lower height

return maxHeight
"""


class Solution(object):
    def maxArea(self, height):

        maxVol = 0

        left, right = 0, len(height) - 1

        while left < right:
            vol = min(height[left], height[right]) * (right - left)

            # if height[left] is lower we want to shift left pointer
            if height[left] < height[right]:
                left += 1

            # MUST be elif so that if false, else does not exectue!
            # https://stackoverflow.com/questions/9271712/difference-between-multiple-ifs-and-elifs
            elif height[right] < height[left]:
                right -= 1
            # if they are equal shift any pointer
            else:
                left += 1

            maxVol = max(vol, maxVol)

        return maxVol


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1, 1]

    print(Solution().maxArea(height))
    print(Solution().maxArea(height2))