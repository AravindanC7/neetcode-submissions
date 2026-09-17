class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1= { ']':'[','}':'{',')':'('}
        for x in  s:
            if x in ('[','{','('):
                stack.append(x)
            else:
                if not stack :
                    return False
                y = stack.pop()
                if y!=dict1[x]:
                    return False
        return not stack


        