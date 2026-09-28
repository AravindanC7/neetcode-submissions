class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2= nums2, nums1
        m = len(nums1)
        n= len(nums2)
        hl = (m+n+1)//2
        l,r = 0,m
        while l<=r:
            
            i= (l+r)//2
            n1_left = nums1[i-1] if i>0 else float("-inf")
            n1_right = nums1[i] if i<m else float("inf")
            j= hl -i
            n2_left = nums2[j-1] if j>0 else float("-inf")
            n2_right = nums2[j] if j<n else float("inf")

            if n1_left<=n2_right and n2_left<=n1_right:
                if (m+n)%2:
                    return max(n1_left,n2_left)
                return (max(n1_left,n2_left) + min(n1_right,n2_right))/2
            elif n1_left>n2_right:
                r=i-1
            else:
                l=i+1
        return 0.0
            



        