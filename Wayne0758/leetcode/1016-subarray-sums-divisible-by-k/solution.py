class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        a=0
        res = 0
        for i in range(len(nums)):
            a = (a+nums[i])%k
            hashmap[a] = hashmap.get(a, 0)+1
        for s in hashmap.values():
            if s>1:
                res+=math.comb(s,2)
        return res
