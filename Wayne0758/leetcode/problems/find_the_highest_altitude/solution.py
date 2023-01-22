class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=[0]
        for i in range(len(gain)):
            b=a[i]+gain[i]
            a.append(b)
        return max(a)