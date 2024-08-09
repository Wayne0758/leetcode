class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap = {}
        res = 0
        for c in word:
            hashmap[c] = hashmap.get(c,0)+1
        hashmap = sorted(hashmap.items(), key = lambda x:x[1],reverse = True)
        count = 0
        times = 1
        for c, n in hashmap:
            if count == 8:
                count =0
                times +=1
            res += times*n
            count +=1
        return res
