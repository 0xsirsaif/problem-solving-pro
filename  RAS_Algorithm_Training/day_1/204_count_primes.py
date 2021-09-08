"""
Count the number of prime numbers less than a non-negative number, n.

notes and review:
- less than only, x is not included
-
TODO
    REVIEW
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        composite_nums = [True] * (n + 1)
        for num in range(2, int(n ** .5) + 1):
            if composite_nums[num]:
                ptr = num * 2
                multi = 3
                while ptr <= n:
                    composite_nums[ptr] = False
                    ptr = num * multi
                    multi += 1

        count = len([i for i in composite_nums[2:n] if i])
        return count



S = Solution()
print(S.countPrimes(30))