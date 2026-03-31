class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length_last_string = 0
        result = 0
        for el in s:
            if el != " ":
                length_last_string+=1
                result = length_last_string
            else:
                length_last_string = 0
                
        return result

        