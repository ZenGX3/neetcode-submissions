class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = nums1
        l2 = nums2
        t = len(nums1)+len(nums2)
        h = t//2
        if len(l1) > len(l2):
            l1, l2 = l2, l1
        l, r = 0, len(l1) - 1
        while True:
            i = (l+r)//2
            j = h-i-2

            l1l = l1[i] if i >= 0 else float("-inf")
            l1r = l1[i+1] if i+1 < len(l1) else float("inf")
            l2l = l2[j] if j >= 0 else float("-inf")
            l2r = l2[j+1] if j+1 < len(l2) else float("inf")

            if l1l <= l2r and l2l <= l1r:
                if t%2:
                    return min(l1r, l2r)
                return (max(l1l, l2l) + min(l1r, l2r))/2
            elif l1l > l2r:
                r = i - 1
            else:
                l = i + 1
        