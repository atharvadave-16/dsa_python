class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = nums1 + nums2
        b = sorted(a)
        m = len(nums1)
        n = len(nums2)
        if (m +n) %2 == 0:
           me = (b[ ((m+n)//2)-1] + b[(m+n)//2]) / 2
        else: me = b[((m +n) // 2)] 
        return me