class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Pass 1: Compute prefix products (store in res)
        # res[i] will contain the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Compute suffix products and multiply with prefix values in res
        # suffix keeps track of the product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res