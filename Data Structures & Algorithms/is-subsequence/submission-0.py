class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if not s: return True
        for elem in range(len(s)):

            for sel in range(i, len(t)):
                if s[elem] == t[sel]:
                    i = sel + 1
                    if elem == len(s) - 1: return True
                    break
            else: return False

        return False
