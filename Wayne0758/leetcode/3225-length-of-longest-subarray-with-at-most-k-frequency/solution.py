class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i, j, n = 0, 0, len(nums)
        cnt = collections.defaultdict(int)
        ans = 0
        while j < n:
            x = nums[j]
            cnt[x] += 1
            j += 1
            while cnt[x] > k:
                cnt[nums[i]] -= 1
                i += 1
            ans = max(ans, j-i)
        return ans
