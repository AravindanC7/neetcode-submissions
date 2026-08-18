class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = {}
        seen = set()
        for i in range(len(numbers)):
            dict1[i+1]=numbers[i]
        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in seen:
                key= [k for k, v in dict1.items() if v ==
                x and k<i+1]
                key.append(i+1)
                return key
            seen.add(numbers[i])
            




            



        