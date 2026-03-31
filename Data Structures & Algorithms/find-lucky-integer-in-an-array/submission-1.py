class Solution:
    def findLucky(self, arr: List[int]) -> int:
        integer = {}
        largest = -1
        for elem in arr:
            
            if elem in integer:
                integer[elem]+=1
            else:
                integer[elem] = 1
        
        for key, value in integer.items():
            
            if key == value :
                if key > largest:
                    largest = key

        for key, value in integer.items():
            if key == value and largest == key:
                return key
        
        return -1