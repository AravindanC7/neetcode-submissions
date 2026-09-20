class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r= len(matrix)-1
        tr=-1
        while l<=r:
            m= (l+r)//2
            if target<matrix[m][0]:
                r= m-1
            elif target >= matrix[m][0] and target<= matrix[m][len(matrix[m])-1]:
                tr=m
                break
            else:
                l=m+1
        if tr == -1:
            return False
        l1=0
        r1= len(matrix[m])-1
        while l1<=r1:
            m1 = (l1+r1)//2
            if target >matrix[tr][m1]:
                l1=m1+1
            elif target <matrix[tr][m1]:
                r1=m1-1
            else:
                return True
        return False
        