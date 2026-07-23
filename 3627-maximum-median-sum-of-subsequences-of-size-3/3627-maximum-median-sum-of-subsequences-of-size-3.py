class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        for i in range(n // 3, n, 2):
            ans += nums[i]

        return ans