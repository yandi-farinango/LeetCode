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
We are given a list of heights, y-coordinates
height[idx] represents x-coordinate 

We want a max container
w a PAIR of max y-coordinates 
&& max x-coordinate
    i.e distance between height values, on the given array 
"""


"""
*** BRUTE FORCE ***

For BRUTE FORCE, 
we can do 2 loops

while we are looping, 
we will calculate vol, 
at each combination
and continuously update resVol 
as max(vol, resVol)

Our loop begins at height[L]
    inner loop starts at height[L+1]
    
    loops will traverse in range(len(height))
    calculate vol as (right - left) * min(height[right], height[left])
    update resVol
    return resVol
"""


"""
*** Linear Time Sol *** 

we will initialize pointers at OPPOSITE ends of height array 
By doing so, we've already maximized x-coor, i.e distance aka Width

While left < right
We will calculate vol same as above 
and update resVol same as above 

THE TRICK HERE, 
We continuously shift pointer 
pointing to smaller height 

if both pointers = same height 
doesnt matter which pointer we shift 

return resVol 
"""


class Solution(object):
    # Brute Force SOL
    # O(n^2)
    def maxAreaBRUTEFORCE(self, height):
        # res variable for container volume
        # will be updated as we go through our loop
        resVol = 0

        for left in range(len(height)):
            # our right pointer will always be
            # 1 position in front of left
            # and will stop at len(height)
            for right in range(left + 1, len(height)):
                # v = W*H
                # width is right - left
                # height = min(left, right)
                vol = (right - left) * min(height[left], height[right])

                resVol = max(vol, resVol)

        return resVol

    def maxArea(self, height):
        # resVol to be updated as we traverse through height array
        resVol = 0

        # set pointers on OPPOSITE ends
        # ***
        # By setting on opposite ends,
        # we are already starting at max distance
        # between x-coords
        left, right = 0, len(height) - 1

        while left < right:
            # vol is calculated the same
            vol = (right - left) * min(height[left], height[right])
            # update is the same
            resVol = max(vol, resVol)

            # if our height at pos LEFT is less than
            # height at pos RIGHT, shift LEFT
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
                # if theyre equal, we can shift either, doesnt matter
            else:
                left += 1

        return resVol



if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1, 1]

    print(Solution().maxAreaBRUTEFORCE(height))
    print(Solution().maxAreaBRUTEFORCE(height2))

    print(Solution().maxArea(height))
    print(Solution().maxArea(height2))