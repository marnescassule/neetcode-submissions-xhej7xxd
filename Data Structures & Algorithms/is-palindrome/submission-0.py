class Solution:
    def isPalindrome(self, s: str) -> bool:
        text_lower = [char.lower() for char in s if char.isalnum()]
        
        return text_lower == text_lower[::-1]
        
        