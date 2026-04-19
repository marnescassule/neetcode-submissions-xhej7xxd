class Solution:
    def tribonacci(self, n: int) -> int:
        cth = 2
        a = 0
        b = 1
        c = 1
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        while cth < n:
            a, b, c = b, c, a + b + c
            cth += 1

        return c