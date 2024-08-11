class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        substrings = []
        tmp = s[0]
        for c in s[1:]:
            if ord(c)-1 == ord(tmp[-1]):
                tmp+=c
            else:
                substrings.append(len(tmp))
                tmp = c
        substrings.append(len(tmp))
        return max(substrings)
