class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val_to_idx = {}
        
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in val_to_idx:
                return [val_to_idx[diff], i + 1]
            val_to_idx[num] = i + 1




            



        