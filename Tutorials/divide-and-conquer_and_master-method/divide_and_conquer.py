"""

"""

from typing import List, Tuple


# brute-force
def counting_inversions_1(arr: List) -> int:
    # O(n^2)
    # the algorithm does a constant number of operations in each loop iteration
    num_of_inversions = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                num_of_inversions += 1

    return num_of_inversions


def counting_inversions_2(arr: List) -> Tuple[int, List]:
    # the combine method
    def count_split_inversions(left_arr: List, right_arr: List) -> Tuple[int, List]:
        merged_arr = [None] * (len(left_arr) + len(right_arr))
        num_of_split_inversions = 0

        k = i = j = 0
        while i < len(left_arr) and j < len(right_arr):
            if left[i] < right[j]:
                merged_arr[k] = left_arr[i]
                i += 1
            else:
                merged_arr[k] = right[j]
                j += 1
                num_of_split_inversions += len(left_arr) - i
            k += 1

        while i < len(left_arr):
            merged_arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            merged_arr[k] = right_arr[j]
            j += 1
            k += 1

        return num_of_split_inversions, merged_arr

    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[0:mid]
        right = arr[mid:]

        c, left = counting_inversions_2(left)
        d, right = counting_inversions_2(right)
        e, sorted_arr = count_split_inversions(left, right)

        return c + d + e, sorted_arr

    return 0, arr


print(counting_inversions_2([6,5,4,3,2,1]))