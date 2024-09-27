class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        mx = 0
        for key in hashmap.keys():
            if hashmap[key]>mx:
                res = key
                mx = hashmap[key]
        return res
