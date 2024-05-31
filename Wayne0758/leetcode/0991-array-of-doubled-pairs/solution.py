class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        hashmap = collections.defaultdict(int)
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        sortedarr = sorted(arr, key = lambda num : abs(num))
        for x in sortedarr:
            if hashmap.get(x) == 0:
                continue
            if hashmap.get(2*x, 0) <= 0:
                return False
            hashmap[x] -= 1
            hashmap[2*x] -= 1
        return True
