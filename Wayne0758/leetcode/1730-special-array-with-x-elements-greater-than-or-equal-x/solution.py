class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [n]
        dp = dp+[0 for _ in range(n)]
        for i in range(1, n+1):
            dp[i]=dp[i-1] - nums.count(i-1)
            if i == dp[i]:
                return i
        return -1
