class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        return (ord(coordinates[0])+int(coordinates[1]))%2==1