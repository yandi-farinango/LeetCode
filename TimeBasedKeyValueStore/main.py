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
        self.store = {} # key : [[value, timestamp]]

    def set(self, key, value, timestamp):
        """
        Stores key with value at a given timestamp

        Ex: set("foo", "bar", 1)
            Key     | Value <val, time>
            "foo"   | [["bar", 1]]

            set("foo", "bar2", 2)
            Key     | Value <val, time>
            "foo"   | [["bar", 1], ["bar2", 2]]

        :param key: str
        :param value: str
        :param timestamp: int
        :return: None
        """

        # if key does not exist in self.store
        # we create key and map it to an empty list
        # ex: key:[]
        if key not in self.store:
            self.store[key] = []

        # append [value, timestamp]
        # ex: key: [[value, timestamp]]
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        Returns a value such that set was called previously with
        timestamp_prev <= timestamp

        If there are multiple such values, returns the value associated with the largest timestamp_prev
        If there are no value, returns ""

        Ex: Key     | Value <val, time>
            "foo"   | [["bar", 1], ["bar2", 2], ["bar6", 6]]

            get("foo", 2)
            return "bar2"

            get("foo", 4)
            return "bar2
                * bar2 is the closest val <= timestamp 4
                return bar2

            We can find the closest val <= timestamp using BINARY SEARCH!!!

        :param key: str
        :param timestamp: int
        :return: str
        """

        # if key doesnt exist,  i.e there are no values
        # return ""
        res = ""

        # return list of values
        # if we don't find a match, return empty list []
        values = self.store.get(key, [])

        # Binary Search
        left, right = 0, len(values)-1

        while left <= right:
            mid = (left + right)//2

            # we are looking for the closest val <= timestamp
            if values[mid][1] <= timestamp:
                # update res
                res = values[mid][0]

                # keep searching, shift left UP
                left = mid + 1
            else:
                right = mid - 1
        return res



if __name__ == '__main__':
    obj = TimeMap()
    obj.set("foo", "bar", 1)

    print(obj.get("foo", 1))
    print(obj.get("foo", 3))

    obj.set("foo", "bar2", 4)

    print(obj.get("foo", 4))
    print(obj.get("foo", 5))