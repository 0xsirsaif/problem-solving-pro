"""
Problem:
    Write a function that reverses a string. The input string is given as an array of characters s.

review and notes:
    - Simultaneous Assignments: TODO

"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        def _swap(ptr1, ptr2):
            temp = s[l]
            s[l] = s[h]
            s[h] = temp

        l, h = 0, len(s) - 1
        while l < h:
            _swap(l, h)
            h -= 1
            l += 1
        print(s)

    def reverseString_2(self, s: List[str]) -> None:
        l, h = 0, len(s) - 1
        while l < h:
            s[l], s[h] = s[h], s[l]
            h -= 1
            l += 1
        print(s)

S = Solution()
print(S.reverseString_2(["h","e","l","l","o"]))