class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) == 1):
            return False

        braces =  {
            "(":")",
            "{":"}",
            "[":"]"
        }

        close = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        parent = []
        open_braces = []

        for el in s:
            if el in braces:
                open_braces.append(el)
                parent.append(braces[el])
            else:
                if(len(open_braces) > 0 and open_braces[-1] == close[el]):
                    open_braces.pop()
                else:
                    return False

        print(parent)
        if len(open_braces) == 0:
            return True
        else:
            return False
        

            