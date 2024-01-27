class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        a = Counter(nums)
        ans=0
        for b in a.values():
            if b == 1:
                return -1
            ans+=(b//3)
            if b % 3:
                ans += 1
        return ans
