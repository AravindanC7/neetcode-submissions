class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 
        r= max(piles)
        res= r
        while l<=r:
            m=(l+r)//2
            t = sum((p+m-1)//m for p in piles)
            if t >h:
                l=m+1
            else:
                res=m
                r=m-1
        return res
            

        