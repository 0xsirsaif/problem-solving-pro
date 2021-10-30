def get_right_dominants(arr):
    dominants = []
    i = len(arr) - 1
    max_num = 0
    while i >= 0:
        if arr[i] > max_num:
            dominants.append(arr[i])
            max_num = arr[i]
        i -= 1
    return dominants


print(get_right_dominants([10, 9, 5, 13, 2, 7, 1, 8, 4, 6, 3]))
