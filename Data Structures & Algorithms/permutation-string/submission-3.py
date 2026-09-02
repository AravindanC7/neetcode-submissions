class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s11 = [0]*26
        s22=[0]*26
        if n1> n2:
            return False
        for r in range(n1):
            s11[ord(s1[r])-ord('a')]+=1
            s22[ord(s2[r])-ord('a')]+=1
        if s11==s22:
            return True
        for r in range(n1,n2):
            s22[ord(s2[r])-ord('a')]+=1
            s22[ord(s2[r-n1])-ord('a')]-=1
            if s11 == s22:
                return True
        return False
        




        