"""
n cars are traveling on a one-lane road

destination is TARGET miles away

their position and speed(mph) are given
as separate arrays

A car can never pass the car in front
BUT
it can catch up to the car
and drive at the same speed
    (the faster car slows to match the speed of the slower)

They are now assumed to have the same position

A CAR FLEET
is a some non-empty set of cars
driving together at same position and same speed

Return the number of fleets that will arrive at destination

    ***NOTE
        * A single car may be considered a fleet

        * If a car catches up to fleet at the destination,
        it will still be considered as one car fleet

"""


class Solution(object):
    def carFleet(self, target, position, speed):

        stack = []

        # creating an array of [position, speed] pairs
        pair = [[position, speed] for position, speed in zip(position, speed)]

        # iterating in reverse sorted order
        for position, speed in sorted(pair)[::-1]:
            # calculating what time we will be reaching
            stack.append((target - position) / speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


if __name__ == '__main__':

    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    target = 12

    print(Solution().carFleet(target, position, speed))
