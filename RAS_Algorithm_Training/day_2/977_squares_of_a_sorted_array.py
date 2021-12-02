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
    - merging technique: (3 whiles, 2 of them being executed)
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

        # F**k
        def __partition(array, start, end):
            pivot = array[start]
            low = start + 1
            high = end

            while True:
                # If the current value we're looking at is larger than the pivot
                # it's in the right place (right side of pivot) and we can move left,
                # to the next element.
                # We also need to make sure we haven't surpassed the low pointer, since that
                # indicates we have already moved all the elements to their correct side of the pivot
                while low <= high and array[high] >= pivot:
                    high = high - 1

                # Opposite process of the one above
                while low <= high and array[low] <= pivot:
                    low = low + 1

                # We either found a value for both high and low that is out of order
                # or low is higher than high, in which case we exit the loop
                if low <= high:
                    array[low], array[high] = array[high], array[low]
                    # The loop continues
                else:
                    # We exit out of the loop
                    break

            array[start], array[high] = array[high], array[start]

            return high

        def _quick_sort(array, start, end):
            if start >= end:
                return

            p = __partition(array, start, end)
            _quick_sort(array, start, p - 1)
            _quick_sort(array, p + 1, end)

            return array

        def __counting_sort(array, place):
            size = len(array)
            output = [0] * size
            count = [0] * 10

            # Calculate count of elements
            for i in range(0, size):
                index = array[i] // place
                count[index % 10] += 1

            # Calculate cumulative count
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Place the elements in sorted order
            i = size - 1
            while i >= 0:
                index = array[i] // place
                output[count[index % 10] - 1] = array[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(0, size):
                array[i] = output[i]

        # Main function to implement radix sort
        def _radix_sort(array):
            max_element = max(array)

            # Apply counting sort to sort elements based on place value.
            place = 1
            while max_element // place > 0:
                __counting_sort(array, place)
                place *= 10

        squared_nums = [i ** 2 for i in nums]
        return _quick_sort(squared_nums, 0, len(squared_nums)-1)


S = Solution()
print(S.sortedSquares([-7, -3, 2, 3, 11]))
