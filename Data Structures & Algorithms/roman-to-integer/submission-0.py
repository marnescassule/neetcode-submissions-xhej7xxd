class Solution:
    def romanToInt(self, s: str) -> int:
        if s[0] == "I":
            number = 1
        elif s[0] == "V":
            number = 5
        elif s[0] == "X":
            number = 10
        elif s[0] == "L":
            number = 50
        elif s[0] == "C":
            number = 100
        elif s[0] == "D":
            number = 500
        elif s[0] == "M":
            number = 1000
        
        for i in range(1,len(s)):
         
             
            if s[i]== 'I':
                number+=1
            elif s[i] == "V" and s[i-1] == "I":
                number+=(5-2)
            elif s[i] == "V":
                number+=5
            elif s[i] == "X" and s[i-1] == "I":
                number+=(10-2)
            elif s[i] == "10":
                number+=(10)
            elif s[i] == "X" and s[i-1] == "I":
                number+=(10-2)
            elif s[i] == "X":
                number+=(10)
            elif s[i] == "L" and s[i-1] == "X" :
                number+=(50-20)
            elif s[i] == "L":
                number+=(50)
            elif s[i] == "C" and s[i-1] == "X" :
                number+=(100-20)
            elif s[i] == "C":
                number+=(100)
            elif s[i] == "D" and s[i-1] == "C" :
                number+=(500-200)
            elif s[i] == "D":
                number+=(500)
            elif s[i] == "M" and s[i-1] == "C" :
                number+=(1000-200)
            elif s[i] == "M":
                number+=(1000) 

        return number