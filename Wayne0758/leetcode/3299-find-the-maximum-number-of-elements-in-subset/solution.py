class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        ans = cnt[1] - (cnt[1] % 2 ^ 1)
        del cnt[1]
        for x in cnt:
            t = 0
            while cnt[x] > 1:
                x = x**2
                t += 2
            if cnt[x]:
                t += 1
            else:
                t -= 1
            ans = max(ans, t)
        return ans
