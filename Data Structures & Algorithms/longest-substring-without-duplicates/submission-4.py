class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r=0
        res=0
        seen= set()
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                res=max(res,(r-l))
                while s[r]!=s[l]:
                    seen.remove(s[l])
                    l+=1
                l+=1
        res=max(res,len(seen))
        return res


        