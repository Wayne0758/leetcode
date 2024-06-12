class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = collections.defaultdict()
        res2=[]
        for num in arr1:
            if num in arr2:
                hashmap[num] = hashmap.get(num, 0) +1
            else:
                res2.append(num)
        res2.sort()
        res=[]
        for num in arr2:
            res += [num for _ in range(hashmap[num])]
        return res+res2
