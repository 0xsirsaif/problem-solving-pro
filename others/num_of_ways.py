"""
Problem (4.2): Dynamic Programming Coding Interview Book
Given a matrix of order N*N. What are the total number of ways in which we can move
    from the top-left cell (arr[0][0] ) to the bottom-right cell (arr[N-1][N-1]),
given that we can only move either downward or rightward?

notes and review:
    - moves:
        - [i+1][j]
        - [i][j+1]
    - how many number reach the last row/column?
    -
TODO:
    CORRECTNESS
    UNITTEST
"""


def num_of_ways(matrix, i, j, ways):
    print(i, j)
    if (i == len(matrix) - 1) or (j == len(matrix) - 1):
        return 1
    ways += num_of_ways(matrix, i + 1, j, ways) + num_of_ways(matrix, i, j + 1, ways)
    return ways


def memo_num_of_ways(matrix, i, j):
    print(i, j)
    if (i == len(matrix) - 1) or (j == len(matrix) - 1):
        memo[i][j] += 1
    elif memo[i][j] == 0:
        memo[i][j] += memo_num_of_ways(matrix, i + 1, j) + memo_num_of_ways(matrix, i, j + 1)

    return memo[i][j]


n_n_matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# print(num_of_ways(n_n_matrix, 0, 0, 0))

n = len(n_n_matrix)
memo = [[0] * n] * n
print(memo_num_of_ways(n_n_matrix, 0, 0))
print(memo)