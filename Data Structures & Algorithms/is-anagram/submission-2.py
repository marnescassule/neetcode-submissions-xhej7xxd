class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_strings_hash = {}
        second_strings_hash = {}
        if(len(s)!= len(t)):
            return False
        
        for character in s:
            if(character in first_strings_hash):
                first_strings_hash[character] += 1
            else:
                first_strings_hash[character] = 1
        
        for character in t:
            if(character in second_strings_hash):
                second_strings_hash[character] += 1
            else:
                second_strings_hash[character] = 1
        
        for key in first_strings_hash:
            if (key in second_strings_hash):
                if first_strings_hash[key] != second_strings_hash[key]:
                    return False
            else:
                return False
        
        return True



        