class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,0
        count1 = {}
        res=[]
        for r in range(k):
            count1[nums[r]]= count1.get(nums[r],0)+1
        res.append(max(count1))

        for r in range(k,len(nums)):
            count1[nums[r]]= count1.get(nums[r],0)+1
            count1[nums[l]]-=1
            
            if count1[nums[l]] == 0:
                del count1[nums[l]]
            l+=1
            res.append(max(count1))
        return res
            





        