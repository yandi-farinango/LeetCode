"""
Design a time-based key-value data structure
that can store multiple values
for the same key
at different time stamps

And, retrieve the key's value
at a certain timestamp

    Ex: Key     | Value <val, time>
        "foo"   | [["bar", 1], ["value2", 2], [...]]

"""

class TimeMap(object):
    def __init__(self):
        self.ans = {}

    def set(self, key, value, timestamp):
        # if key is not in our dictionary,
        # create empty list where we will be appending [value, timestamp]
        if key not in self.ans:
            self.ans[key] = []

        self.ans[key].append([value, timestamp])


    def get(self, key, timestamp):
        ans = ""

        # getting list of values associated with key
        values = self.ans.get(key, [])

        # now we want to search through values
        # and return the value with the closest matching timestamp to timestamp

        # initialize pointers
        left, right = 0, len(values) - 1

        # Binary Search
        while left <= right:
            mid = (left + right)//2

            if values[mid][1] <= timestamp:
                # update ans
                ans = values[mid][0]

                # keep searching, shift left UP
                left = mid + 1
            else:
                # search down
                right = mid - 1

        return ans


if __name__ == '__main__':
    obj = TimeMap()
    obj.set("foo", "bar", 1)

    print(obj.get("foo", 1))
    print(obj.get("foo", 3))

    obj.set("foo", "bar2", 4)

    print(obj.get("foo", 4))
    print(obj.get("foo", 5))