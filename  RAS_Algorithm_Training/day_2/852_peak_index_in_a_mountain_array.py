"""
Let's call an array `arr` a mountain if the following properties hold:
    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... arr[i-1] < arr[i]
        - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array `arr` that is guaranteed to be a mountain,
return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Thinking:
- all you need is to find the index of the largest element?__ Yup
- what about binary search?
    - find the first element that arr[i] > arr[i+1]? or
    - find the last element that arr[i] > arr[i-1]?
    - (Start <= End) -> (Start < End)?
    -
- Golden-section search? TODO

review and notes:
TODO
"""

from typing import List


class Solution:
    # binary search
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start

    # Boom!
    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        return arr.index(max(arr))

    # Golden-section search
    def peakIndexInMountainArray3(self, arr: List[int]) -> int:
        pass


S = Solution()
print(S.peakIndexInMountainArray([0, 1, 0]))
