class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = collections.defaultdict(int)
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0)+1
        flag=0
        res=0
        for c in hashmap.keys():
            if hashmap[c]%2==0:
                res+=hashmap[c]
            else:
                res += (hashmap[c]-1)
                if flag==0:
                    res+=1
                    flag=1
        return res
