class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        s = [1]*n
        s2= [1]*n
        s3=[1]*n
        for i in range(1,len(nums)):
            s[i] = nums[i-1]*s[i-1]
        for i in range(len(nums)-2,-1,-1):
            s2[i] = nums[i+1]*s2[i+1]
        for i in range(0,len(nums)):
            s3[i] = s[i]*s2[i]
        return s3

