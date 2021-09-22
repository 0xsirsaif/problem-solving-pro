"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.

TODO:
    OPTIMIZATION
    REVIEW
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = dict()
        for idx, value in enumerate(nums):
            if (value in store) and abs(idx - store[value]) <= k:
                return True
            store[value] = idx
        return False
