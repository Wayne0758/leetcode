class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = list(nums)
        res = -float('inf')
        for i in range(1,n):
            dp[i] += dp[i-1]
        di = {}
        for i in range(len(nums)):
            if nums[i]-k in di:
                y = di[nums[i]-k]
                if y!=0:
                    res = max(res,dp[i] - dp[y-1])
                else:
                    res = max(res,dp[i])
            if nums[i]+k in di:
                y = di[nums[i]+k]
                if y!=0:
                    res = max(res,dp[i] - dp[y-1])
                else:
                    res = max(res,dp[i])
            if(nums[i] in di):
                curr = 0
                if(di[nums[i]] != 0):
                    curr = di[nums[i]]-1
                
                if(dp[curr] > dp[i-1]):
                    di[nums[i]] = i
            else:
                di[nums[i]] = i
        if res == -float('inf'):
            return 0
        return res
