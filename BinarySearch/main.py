# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) -1

        while left <= right:
            mid = (right+left)//2

            if target > nums[mid]:
                left = mid +1
            elif target < nums[mid]:
                right = mid -1
            else:
                return mid
        return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9

    #print(len(nums))
    print(Solution().search(nums, target))


