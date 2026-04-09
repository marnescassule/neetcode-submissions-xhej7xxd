class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        start = 0 
        end = len(s) -1

        while(start < end):
            aux_a = s[start]
            aux_b = s[end]
            s[start] = aux_b
            s[end] = aux_a

            start+=1
            end-=1
        
        return s
        