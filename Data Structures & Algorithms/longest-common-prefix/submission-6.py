class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        frst_word = strs[0]
        str_result = ""

        for idx in range(len(frst_word)):
            char = frst_word[idx]
            count = 1
            for elem in range(1,len(strs)):
                if(len(strs[elem])> idx):
                    if char == strs[elem][idx]:
                        count+=1
            
            if count == len(strs):
                str_result+=char
            else:
                return str_result

        return str_result