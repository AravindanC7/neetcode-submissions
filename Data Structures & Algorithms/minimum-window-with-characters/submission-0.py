class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_count= {}
        have=0
        l,j=0,0
        res = [-1, -1]
        res_len = float("inf")
        curr_count ={}
        for x in t:
            window_count[x]= window_count.get(x,0)+1
        for j in range(len(s)):
            curr_count[s[j]]= curr_count.get(s[j],0)+1
            if s[j] in window_count and curr_count[s[j]] == window_count[s[j]]:
                have+=1
            while have == len(window_count):
                if (j-l+1)< res_len:
                    res=[l,j]
                    res_len=j-l+1
                curr_count[s[l]]-=1
                if s[l] in window_count and  curr_count[s[l]] < window_count[s[l]]:
                    have-=1
                l+=1
        return s[res[0] : res[1] + 1] if res_len != float("inf") else ""

                
                







        
        