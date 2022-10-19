"""
Given a characters array, Tasks,
representing tasks a CPU needs to perform

each letter corresponds to a different task

Tasks may be done in any order

Each task is done in 1 unit of time

For each unit of time,
the CPU can complete either 1 task or be idle


There is a non-negative int, n,
represents the cool down, ie idle period,
between two SAME tasks

Return the least number of times
the CPU will take to finish
all given tasks


    Ex:
    ['A', 'A', 'A', 'B', 'B', 'B']
    n = 2

    output: 8

            AB_AB_AB   <- size = 8
            We have to wait 2 units of time before processing another same char

"""
import collections
import heapq
from collections import Counter

"""
To solve this

We'll want get charCounts 
we'll can do this using counter function 

We'll want to start processing the most frequent task first 
in order to do this, 
we'll be using a maxHeap 

We can add charCounts to our maxHeap 
and pop the most frequent 

When we pop the most frequent, 
we'll want to append char to a que, 
in order to keep track of idle times

We'll be appending [-count, idleTime] to our que 


"""


class Solution(object):
    def leastInterval(self, tasks, n):
        # get charCount
        charCount = Counter(tasks)

        # initialize maxHeap
        maxHeap = [-count for count in charCount.values()]
        heapq.heapify(maxHeap)

        # initialize time counter
        time = 0

        # initialize que
        que = collections.deque()

        # processing
        while maxHeap or que:
            # increment timer
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    que.append([cnt, time + n])

            if que and que[0][1] == time:
                heapq.heappush(maxHeap, que.popleft()[0])

        return time


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    print(Solution().leastInterval(tasks, n))
