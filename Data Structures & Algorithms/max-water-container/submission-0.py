class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        cap = 0
        while i<j:
            if heights[i]>heights[j]:
                cap= max(cap,(heights[j]*(j-i)))
                j-=1
            else :
                cap= max(cap,(heights[i]*(j-i)))
                i+=1

        return cap



        