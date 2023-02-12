class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if s[::-1]==s:
            return 1
        else:
            return 2
