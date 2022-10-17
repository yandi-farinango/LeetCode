"""
Given
an array of points where
points[i] = [xi, yi]

and an integer k

return the k closest points
to the origin (0,0)

Distance between points
√x^2 + y ^2

"""
import heapq

"""
We can solve this problem using a minHeap 

We'll have a res variable 


we'll want to loop 
for x, y in distance 
we want to set up our minHeap such that it follows 
distance, x, y
minHeap.append(distance, x, y)


We'll be popping from our heap k times 
so we want our first values to be the distance to the origin 

while k > 0 
we'll pop distance, x, y from our minHeap
and append([x, y]) 
decrement k


"""

class Solution(object):
    def KClosest(self, points, k):

        # initialize res
        res = []

        # initialize minHeap
        minHeap = []

        for x, y in points:
            distance = (x**2) + (y**2)
            minHeap.append([distance, x, y])

        # heapify minHeap
        heapq.heapify(minHeap)

        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])

            # decrement counter
            k -= 1

        return res


if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    k = 1

    print(Solution().KClosest(points, k))