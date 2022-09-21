"""
n cars going to same destination
on a one-way road

destination is target miles away

given
    position array      i.e position[i] = position of ith car
    speed array         i.e array[i] = speed of ith car


Cars can never pass one another
But can catch up and drive bumper2bumper

    * if slower car is in front
    faster car will catch up
    but then
    slow down to match slower cars speed

These cars are assumed to have the same position


A car fleet is some non-empty set of cars
driving at same position and speed


Return number of car fleets that will arrive at destination

    * a single car may be considered a car fleet

    * if a car catches up to a car fleet right at the destination,
    it is considered as part of the fleet
"""

"""
To solve this problem

We need to know what time cars will be reaching the destination 

Also, we'll need to sort the cars by their respective position
b/c 
if the car in a behind pos 
is to reach the destination 
earlier than the car in front, this will become a car fleet

at this point we can disregard the car 
which should is to arrive earlier 
b/c it will actually SLOW to match the speed of the car in front 


We can set this up using a stack!! 


As mentioned above, we'll need to sort the cars by their respective pos
it would be a good idea to maintain each pos together w respective speed 

We can create pair array where [(pos, speed)]

From there we can sort our pair array 
We will now have a sorted array of [pos, speed]

We can traverse sorted pair array in reverse 

append time to reach destination to our stack 
    * time to destination = (target - pos) / speed

if we have at least 2 cars in our stack,
and our current car's arrival           i.e stack[-1]
is less than car in front's arrival     i.e stack[-2]

we can pop current car from our stack 
since it becomes a fleet w car in front i.e stack[-2]
    * as mentioned above, 
    we pop the car that would technically arrive earlier b/c 
    it actually will slow down to match the speed of the car in front of it 

we return len of stack 
"""


class Solution(object):
    def carFleet(self, target, position, speed):

        stack = []

        pos = [[pos, speed] for pos, speed in zip(position, speed)]
        pos.sort()

        for pos, speed in pos[::-1]:

            # calculate expected arrival time
            stack.append((target - pos) / speed)

            # if current car                        i.e stack[-1]
            # arrives earlier than previous car     i.e stack[-2]
            # stack[-1] < stack[-2]
            # we pop from our stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


""""
Another implementation 
"""


class Solution2(object):
    def carFleet(self, target, position, speed):
        zipped = [[pos, speed] for pos, speed in zip(position, speed)]
        zipped.sort()


        stack = []

        for car in zipped[::-1]:
            est = (target - car[0]) / car[1]

            while stack and stack[-1] >= est:
                stack.pop()

            stack.append(est)

        return len(stack)


if __name__ == '__main__':

    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    target = 12

    pos2 = [6, 8]
    speed2 = [3,2]
    target2 = 10



    print(Solution().carFleet(target, position, speed))
    print(Solution().carFleet(target2, pos2, speed2))

    print(Solution2().carFleet(target, position, speed))
    print(Solution2().carFleet(target2, pos2, speed2))
