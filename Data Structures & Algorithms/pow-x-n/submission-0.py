class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = True
        if n < 0:
            p = False
            n = abs(n)
        res = 1
        count = 1

        while(count <= n):
            res*=x
            count+=1
        
        if p:
            return res
        else:
            return float(1/res)
