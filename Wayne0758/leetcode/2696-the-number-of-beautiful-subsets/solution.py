class Solution:
    def __init__(self):
        self.hashmap = collections.defaultdict()
        self.res = 0
    def helper(self, nums: List[int], k: int, start: int) -> int:
        if self.hashmap:
            self.res+=1
        for i in range(start, len(nums)):
            if (nums[i]+k) in self.hashmap.keys() or (nums[i]-k) in self.hashmap.keys():
                continue
            if nums[i] in self.hashmap.keys():
                self.hashmap[nums[i]] += 1
            else:
                self.hashmap[nums[i]] = 1
            self.helper(nums, k, i+1)
            self.hashmap[nums[i]] -= 1
            if self.hashmap[nums[i]] == 0:
                del self.hashmap[nums[i]]
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.helper(nums, k, 0)
        return self.res
