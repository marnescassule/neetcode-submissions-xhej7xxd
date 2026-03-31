class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        idx = len(arr) -1
        
        while(idx >= 0):
            temp = arr[idx]
            arr[idx] = max_val

            if(max_val < temp):
                max_val = temp
        
            idx -= 1
        return arr
            
