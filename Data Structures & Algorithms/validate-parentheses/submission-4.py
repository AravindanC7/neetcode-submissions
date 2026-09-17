class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1= { ']':'[','}':'{',')':'('}
        for x in  s:
            if x in dict1:
                if not stack :
                    return False
                top = stack.pop()
                if top != dict1[x]:
                    return False
            else:
                stack.append(x)
        return not stack
        