"""
Given a chars array, Tasks,
representing tasks
a CPU needs to perform

where each letter is a different task

tasks can done in any order

Each task takes one unit of time to execute


During a unit of time,
the computer can either complete one task
or be on idle


There is also a non-negative int, n,
that represents the cool down period
between two same tasks (ie same letter in Tasks array)

ie the computer must wait
n units of time
before performing any two same tasks

Return the least number of units of time
that the CPU will take
to finish all the given tasks


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
we'll do this using counter function 

We'll want to continuously the most frequent task first 
ie after we've processed a task, we reduce the count 

in order to do continuously process the most frequent, 
we'll be using a maxHeap 

we'll use a time counter,
initialized time = 0,
to keep track of time 

We'll pop from our maxHeap
decrement the charCount and 
increment our time counter 

we'll also be keeping track 
of when we'll be able to process 
another task of the same type ie same char 

we can determine when a task is available
to process again 
by adding idle time at time task was processed 

we'll use a que 
to append(updatedCount after processing, time task can be processed again)

when we reach a time 
where tasks in our que 
are available to be processed again, 
we'll pop from our que 
and add them back to our maxHeap 

when a tasks charCount reaches 0 
we no longer have to add it to our que 

return time 


* bc python doesnt have a maxHeap 
we'll actually use a minHeap 
but we'll make all counts negative 
"""


class Solution(object):
    def leastInterval(self, tasks, n):

        # get charCount
        charCount = Counter(tasks)

        # initialize maxHeap with negative counts
        maxHeap = [-count for count in charCount.values()]
        heapq.heapify(maxHeap)

        # initialize que
        que = collections.deque()

        # initialize time counter
        time = 0

        while maxHeap or que:
            # increment time counter at each iteration
            time += 1

            # pop most frequent
            # and decrement cnt
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                # append [cnt, time + idle] to que
                if cnt:
                    que.append([cnt, time + n])

            # when we reach a time
            # such that a task can be processed again,
            # we pop from our que and add it back to maxHeap
            if que and que[0][1] == time:
                heapq.heappush(maxHeap, que.popleft()[0])   # we only need to add cnt

        return time



if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    print(Solution().leastInterval(tasks, n))
