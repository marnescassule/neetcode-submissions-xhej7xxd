class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        result = 0

        for elem in details:
            if(int(elem[11:13])> 60):
                result += 1

        return result 

