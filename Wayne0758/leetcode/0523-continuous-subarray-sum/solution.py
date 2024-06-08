class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        a=0
        hashmap = collections.defaultdict()
        hashmap[0] = -1
        for j in range(len(nums)):
            a = (a+nums[j])%k
            hashmap[a] = hashmap.get(a, j)
            if j-hashmap[a] > 1:
                return True
        return False
