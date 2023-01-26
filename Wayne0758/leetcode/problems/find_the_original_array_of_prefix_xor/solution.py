class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        a=[pref[0]]
        for i in range(1,len(pref)):
            a.append(pref[i]^pref[i-1])
        return a