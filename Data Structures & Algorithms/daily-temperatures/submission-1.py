class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack =[]
        result =[0]*n
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                k=stack.pop()
                result[k] = i-k
            stack.append(i)
        return result


            

        