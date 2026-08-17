class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_streak =0

        for num in set_nums:
            if (num-1) not in set_nums:
                curr = num
                curr_streak =1
                while curr+1 in set_nums:
                    curr+=1
                    curr_streak+=1
                longest_streak = max(longest_streak,curr_streak) 
        return longest_streak


        