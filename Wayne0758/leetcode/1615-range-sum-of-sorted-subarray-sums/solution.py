class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new = []
        for i in range(n):
            for j in range(i+1,n+1):
                new.append(sum(nums[i:j]))
        new = sorted(new)
        return sum(new[left-1:right])%1000000007
