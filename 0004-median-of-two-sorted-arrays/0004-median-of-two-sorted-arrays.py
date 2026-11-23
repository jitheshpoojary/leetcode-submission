class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        n = len(arr)
        
        if n % 2 == 0:
            mid = n // 2
            return (arr[mid-1] + arr[mid]) / 2.0
        else:
            return arr[n // 2]
