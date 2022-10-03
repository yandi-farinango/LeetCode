"""
We are given piles array
containing the number of piles given
piles[i] has i bananas

h is the number of hours until the guard returns

Koko can eat k bananas / hour

each hour koko chooses a pile
and eats k bananas from that pile

if the pile has less than k bananas,
Koko will ONLY eat all the bananas from that pile
w/o moving on to the next pile

i.e Koko will eat one pile / hour

    * piles.length <= h

return min speed k
where Koko can eat all piles in h hours

***on the first example

If we try k = 1

h = 8
piles = [3, 6, 7, 11]

it would take us 3/1 + 6/1 + 7/1 + 11/1
17hours


If we try k = 11

h = 8
piles = [3, 6, 7, 11]

it would take us 3/11 + 6/11 + 7/11 + 11/11
4HOURS  * Koko will eat at most one pile/hour
"""

"""
So we are looking for a K value 
from 1 - max(piles)
that will allow us to eat all the bananas 
in <= h hours


We can apply a binary search to k!!

** on example 1 
k ranges 1-11

if we try binary search on k 

k middle rate = 6 

at rate =6 
Koko can eat 
3/6 + 6/6 + 7/6 + 11/6 

6HOURS * we do round up division 

6Hours <= h 

But we are looking for min rate 
So we continue binary search on range of k values 


So to do our binary search through K 
we start with our pointers on opposite ends

    K ranges from 1 - max(piles)
    
We initially set an ans variable = right i.e at max(piles) Koko will eat all bananas 

While left < right:
K is set at midpoint range  ie left + right //2

We have a counter for hours
And get the hours it would take for us to go through the bananas in each pile 

If hour hours < h, we have a valid solution 
We can update our ans variable to a new min 

And now we can shift our right pointer down 
Since we want to continuously search for smaller K rates 

else we're eating too slow 
so we shift our left pointer 

return ans 
"""
import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        ans = right

        while left < right:
            # midpoint
            k = (left + right) // 2

            # hours counter
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                # we are searching for the min K
                ans = min(k, ans)

                # shift right pointer
                # to keep searching for a smaller val
                right = k - 1

            # else rate is too slow
            # we need to shift left pointer
            else:
                left = k + 1

        return ans

class Solution2(object):
    def minEatingSpeed(self, piles, h):
        """
        LeetCode has issues w math.ceil
        implemented solution w/o math.ceil
        """

        left, right = 0, max(piles)
        ans = right

        while left <= right:
            k = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += ((pile - 1) // k) + 1
            if hours <= h:
                ans = min(ans, k)
                right = k - 1
            elif hours > h:
                left = k + 1
        return ans

if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8

    piles2 = [30, 11, 23, 4, 20]
    h2 = 5

    piles3 = [30, 11, 23, 4, 20]
    h3 = 6

    print(Solution().minEatingSpeed(piles, h))
    print(Solution().minEatingSpeed(piles2, h2))
    print(Solution().minEatingSpeed(piles3, h3))

    print(Solution2().minEatingSpeed(piles, h))
    print(Solution2().minEatingSpeed(piles2, h2))
    print(Solution2().minEatingSpeed(piles3, h3))
