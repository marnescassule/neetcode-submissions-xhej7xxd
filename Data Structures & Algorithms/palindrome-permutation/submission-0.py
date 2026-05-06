class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)
        odd_counts = 0
        for char in counts:
            if counts[char] % 2 != 0:
                odd_counts += 1

        return odd_counts <= 1