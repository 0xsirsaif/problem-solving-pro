"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

TODO
    RECURSION VERSION
    REVIEW
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            print(start, end)
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1


S = Solution()
print(S.search(nums=[-1,0,3,5,9,12], target=2))
