class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        fac = []
        for x in range(1, isqrt(n) + 1):
            if n % x == 0:
                fac.append(x)
                if n // x != x:
                    fac.append(n // x)
                    
        target = sorted(nums)
        
        def kmp(nums1, nums2):
            n, m = len(nums1), len(nums2)
            pi = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and nums2[i] != nums2[j]:
                    j = pi[j - 1]
                if nums2[i] == nums2[j]:
                    j += 1
                pi[i] = j
                
            j = 0
            for i in range(n):
                while j > 0 and nums1[i] != nums2[j]:
                    j = pi[j - 1]
                if nums1[i] == nums2[j]:
                    j += 1
                if j == m:
                    return True
            return False

        ans = 0
        for d in fac:
            can_sort = True
            for i in range(0, n, d):
                if not kmp(nums[i:i + d] * 2, target[i:i + d]):
                    can_sort = False
                    break
            if can_sort:
                ans += d
                
        return ans