"""
Given an integer array nums, find the contiguous sub-array (containing at least one number)
which has the largest sum and return its sum.

TODO:
    Kadane's algorithm
    REVIEW
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for x in range(1, len(nums)):
            if nums[x-1] > 0:
                nums[x] += nums[x-1]
        return max(nums)


S = Solution()
print(S.maxSubArray([-1]))