class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        area=0
        heights.append(0)
        for i,x in enumerate(heights):
            if not stack:
                stack.append(i)
            if x>= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]]>x:
                    h= heights[stack.pop()]
                    r= i
                    l=(stack[-1] if stack else -1)
                    w=r-l-1
                    area = max(area,(h*w))
                stack.append(i)
        return area
        