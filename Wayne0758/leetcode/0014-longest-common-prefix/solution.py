class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            temp = 1
            for j in range(1, len(strs)):
                if len(strs[j])<=i:
                    return res
                if strs[0][i] != strs[j][i]:
                    return res
            if temp == 1:
                res += strs[0][i]
        return res
