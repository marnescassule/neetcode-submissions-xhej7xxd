class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6"
        }
        rotate_new_number = ""
        str_nr = str(n)
        idx = len(str_nr) - 1
        while(idx >= 0):
            if str_nr[idx] not in rotate:
                return False
            else: 
                rotate_new_number += rotate[str_nr[idx]]
            
            idx-=1
        if(int(rotate_new_number) == n):
            return False

        return True
        

