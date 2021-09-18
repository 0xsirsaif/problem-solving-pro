"""
Problem:
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).

TODO: efficient solution
review and notes:
    TODO
"""

from typing import List


class Solution:
    # brute-force solution
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def _merge_sorted_lists(arr1, arr2):
            array = [0] * (len(arr1) + len(arr2))
            i = j = k = 0

            # Until we reach either end of either L or M, pick smaller among
            # elements L and M and place them in the correct position at A[p..r]
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    array[k] = nums1[i]
                    i += 1
                else:
                    array[k] = nums2[j]
                    j += 1
                k += 1

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            while i < len(nums1):
                array[k] = nums1[i]
                i += 1
                k += 1

            while j < len(nums2):
                array[k] = nums2[j]
                j += 1
                k += 1

            return array

        merged_array = _merge_sorted_lists(nums1, nums2)
        median_element = len(merged_array) // 2
        is_odd = len(merged_array) % 2
        if not is_odd:
            return float(sum(merged_array[median_element - 1: median_element + 1])/2)

        return float(merged_array[median_element])


S = Solution()
print(S.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
