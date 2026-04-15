class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for elm in range(len(s)-1):
            res += abs(ord(s[elm]) - ord(s[elm +1]))

        return res