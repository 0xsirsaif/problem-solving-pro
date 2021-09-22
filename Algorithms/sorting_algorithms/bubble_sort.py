"""
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

TODO: UNITTEST
"""

def _swap(arr, i):
    temp = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = temp
    return arr


def iterative_bubble_sort(arr):  # O(n^2)
    arr_len = len(arr) - 1
    for cycle in range(arr_len):
        for i in range(arr_len):
            if arr[i] > arr[i + 1]:
                _swap(arr, i)
    return arr


def recursive_bubble_sort(arr, cycle):
    if cycle == 0:
        return arr
    arr_len = len(arr) - 1
    for i in range(arr_len):
        if arr[i] > arr[i + 1]:
            _swap(arr, i)

    return recursive_bubble_sort(arr, cycle - 1)


nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(iterative_bubble_sort(nums))
print(recursive_bubble_sort(nums, len(nums) - 1))
