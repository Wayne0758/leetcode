class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        a=[first]
        b=first
        for i in range(len(encoded)):
            b=encoded[i] ^ b
            a.append(b)
        return a