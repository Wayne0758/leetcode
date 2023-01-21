class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n=s
        for i in range(len(s)):
            index=indices[i]
            n=n[:index] + s[i] + n[index+1:]
        return n
