class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        a = 0
        for num in nums:
            a = a|num
        a = bin(a)
        for i in range(len(a)):
            if a[i]=='1':
                res += (2**(len(nums)-1))*(2**(len(a)-i-1))
        return res
