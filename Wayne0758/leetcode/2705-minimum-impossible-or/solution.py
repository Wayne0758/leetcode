class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        i=0
        while True:
            if 2**i not in nums:
                return 2**i
            i+=1
