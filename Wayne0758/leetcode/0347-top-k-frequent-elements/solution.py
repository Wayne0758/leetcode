class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        hashmap = sorted(hashmap.items(), key = lambda item:item[1], reverse = True)
        res = []
        for i in range(k):
            res.append(hashmap[i][0])
        return res
