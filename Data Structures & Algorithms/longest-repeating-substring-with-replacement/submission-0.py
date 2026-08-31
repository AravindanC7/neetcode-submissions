class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        freq=0
        dict1={}
        for r in range(len(s)):
            dict1[s[r]] = dict1.get(s[r],0)+1
            freq= max(freq,dict1[s[r]])
            
            while (((r-l)+1) -freq)>k:
                dict1[s[l]] = dict1[s[l]] -1
                l+=1
            res= max(res,(r-l+1))
        return res








        