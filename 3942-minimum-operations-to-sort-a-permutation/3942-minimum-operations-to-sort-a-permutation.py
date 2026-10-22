
class Solution:
    def minOperations(self, nums):
        n = len(nums)
        k = nums[0]

        if all(nums[i] == (i + k) % n for i in range(n)):
            return min(n - k, k + 2) if k != 0 else 0

        k = (nums[0] + 1) % n

        if all(nums[i] == (nums[0] - i) % n for i in range(n)):
            return 1 + min(k, n - k)

        return -1
