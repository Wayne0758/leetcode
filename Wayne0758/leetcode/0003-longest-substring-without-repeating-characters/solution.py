class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        i = 0
        j = 0
        mx = 0
        while j<len(s):
            hashmap[s[j]] += 1

            while hashmap[s[j]]>1:
                hashmap[s[i]] -= 1
                i += 1
            mx = max(mx,(j-i+1))
            j+=1
        return mx
