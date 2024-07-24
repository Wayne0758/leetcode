class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
        print(hashmap)
        sorted_decreasing_hashmap = dict(sorted(hashmap.items(), key = lambda x:x[0], reverse = True))
        sorted_hashmap = dict(sorted(sorted_decreasing_hashmap.items(), key = lambda x:x[1]))
        for key in sorted_hashmap.keys():
            for i in range(sorted_hashmap[key]):
                res.append(key)
        return res
