"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

notes and review:
- insertion sort:
    - assume that the first item s already sorted, and start from the second item
    - from index(num - 1) to 0
    - num is inserted after the while loop finishes
    -

- bubble sort
    - loop n rounds over the array, for each round swap every inversion you face > swap(arr[i], arr[i+1]).
    - in the round Y, the Yth largest element is at the right position.
    - after the k rounds, the k largest items are in the right position.
        - first round -> the largest item is at the end of the arr.
        - fifth round -> the largest 5 items are at the end of the arr.
        - ...
    - The number of inversions indicates how much work is needed to sort the array, thus the complexity of the algorithm
        - worst case (reversed array) -> inversions = 1 + 2 + 3 + .... + (n-1) = n(n-1)/2 -> O(n^2)
    - how many swaps = time complexity

- Merge sort
    - divide and conquer, buddy
    - divide until each sublist contains one element, then return it to be merged.
    - merging technique:
        - step 1: compare elements in each array, and move pointers until you reach the end of one of them
            - maintain pointer for each array (left, right, original)
            - pick the smaller element and place it in the original pointer
        - step 2: add the remaining elements of the non-consumed sub array
            - two while blocks to tie the remaining elements, only one block will be executed
- Counting sort
    - TODO
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def _insertion_sort(array):  # O(n^2)
            for step in range(1, len(array)):  # O(n)
                num = array[step]
                ptr = step - 1

                while ptr >= 0 and num < array[ptr]:  # O(n)
                    array[ptr + 1] = array[ptr]
                    ptr = ptr - 1

                array[ptr + 1] = num
            return array

        def _bubble_sort(array):  # O(n^2)
            through = len(array) - 1
            for round in range(through):
                for i in range(through):
                    if array[i] > array[i + 1]:
                        temp = array[i]
                        array[i] = array[i + 1]
                        array[i + 1] = temp
            return array

        def _merge_sort(array):  # O(nlogn)
            if len(array) > 1:
                mid = len(array) // 2
                left = array[:mid]
                right = array[mid:]

                _merge_sort(left)
                _merge_sort(right)

                i = j = k = 0

                # Until we reach either end of either L or M, pick smaller among
                # elements L and M and place them in the correct position at A[p..r]
                print(array, left, right)
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i += 1
                    else:
                        array[k] = right[j]
                        j += 1
                    k += 1

                # When we run out of elements in either L or M,
                # pick up the remaining elements and put in A[p..r]
                while i < len(left):
                    array[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    array[k] = right[j]
                    j += 1
                    k += 1

            return array

        def _counting_sort(array):  # O(n)
            size = (max(array) + 1)
            counting_tree = [0] * size

            for num in array:  # O(n)
                counting_tree[num] += 1

            # cumulative sum
            for i in range(1, size):  # O(n)
                counting_tree[i] += counting_tree[i - 1]

            sorted_array = [0] * len(array)
            i = len(array) - 1
            while i >= 0:   # O(n)
                num = array[i]
                counting_tree[num] -= 1
                idx = counting_tree[num]
                sorted_array[idx] = num
                i -= 1

            return sorted_array

        squared_nums = [i ** 2 for i in nums]
        return _counting_sort(squared_nums)


S = Solution()
print(S.sortedSquares([-7, -3, 2, 3, 11]))
