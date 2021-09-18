"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

TODO
    find good algorithms for element frequency
    REVIEW
"""

from typing import List


class Solution:
    # brute-force
    def majorityElement(self, nums: List[int]) -> int:
        frequency_map = {k: 0 for k in nums}
        for i in nums:
            frequency_map[i] += 1

        return max(frequency_map.keys(), key=(lambda key: frequency_map[key]))


S = Solution()
print(S.majorityElement([6,5,5]))