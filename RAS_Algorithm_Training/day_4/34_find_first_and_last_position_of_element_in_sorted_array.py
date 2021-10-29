"""
Problem:
    Given an array of integers nums sorted in ascending order,
    find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.

review and notes:
    Algorithm 1:
        - find the first element <= target
            - start = index + 1
        - find the first element >= target
            - end = index - 1

"""

from typing import List

from collections import Counter


class Solution:
    # bad, very bad
    def searchRange_bad(self, nums: List[int], target: int) -> List[int]:
        def _binary_search(arr, start, end, num):
            if start > end:
                return [-1, -1]

            mid = (start + end) // 2

            if arr[mid] == num:
                counter = dict(Counter(arr))
                before_target = sum([counter[x] for x in counter if x < num])
                after_target = len(arr) - before_target - counter[num]
                return [before_target, len(arr) - after_target - 1]
            elif num > arr[mid]:
                return _binary_search(arr, mid + 1, end, num)
            elif num < arr[mid]:
                return _binary_search(arr, start, mid - 1, num)

        return _binary_search(nums, 0, len(nums) - 1, target)

    # not bad, but...
    def searchRange(self, nums: List[int], target: int) -> List[int]:   # O(2 log n)
        def _first_index(arr):  # O(log n)
            low, high = 0, len(arr) - 1
            answer = -1
            while low <= high:
                mid = low + ((high - low) // 2)
                if arr[mid] >= target:
                    answer = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return answer

        def _last_index(arr):  # O(log n)
            low, high = 0, len(arr) - 1
            answer = -1
            while low <= high:
                mid = low + ((high - low) // 2)
                if arr[mid] <= target:
                    answer = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return answer

        first = _first_index(nums)
        last = _last_index(nums)
        if (last < first) or (first < 0) or (last < 0):
            return [-1, -1]
        return [first, last]


S = Solution()
print(S.searchRange([5,7,7,8,8,10], 8))