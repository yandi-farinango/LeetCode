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
We can solve this using a minHeap 

We'll have a res variable = []
where we'll be appending the coordinates of the kth closest point

and we'll want to loop 
for x, y 

We'll be appending distance from origin
to our minHeap 
minHeap.append([distance, x, y])

in order to get the kth closest point to the origin, 
we'll need to pop from our minHeap k times 

we can say
while k > 0 
    we pop distance, x, y from our minHeap
    append [x, y] to res

    decrement k -=1 

return res

"""

class Solution(object):
    def KClosest(self, points, k):

        # initialize res
        res = []

        # minHeap variable
        minHeap = []

        # populate and heapify minHeap
        for x, y in points:
            # append to minHeap
            minHeap.append([(x ** 2) + (y ** 2), x, y])

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