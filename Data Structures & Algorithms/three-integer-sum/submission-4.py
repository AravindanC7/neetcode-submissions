class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        res=[]
        for i in range(len(nums_sort)):
            if nums_sort[i]>0:
                break
            if i > 0 and nums_sort[i] == nums_sort[i-1]:
                continue
            l,r = i+1, len(nums_sort)-1
            while l<r:
                s = nums_sort[i] +nums_sort[l]+nums_sort[r]
                
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    res.append([nums_sort[i],nums_sort[l],nums_sort[r]])
                    l+=1
                    r-=1
                    while l<r and  nums_sort[l]== nums_sort[l-1]:
                        l+=1
                    while l<r and nums_sort[r] == nums_sort[r+1]:
                        r-=1

        return res
