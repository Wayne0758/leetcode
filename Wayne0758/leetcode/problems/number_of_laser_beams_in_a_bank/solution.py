class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        a=0
        s=0
        for i in range(len(bank)):
            if '1' in bank[i]:
                b=bank[i].count('1')
                s+=a*b
                a=b
        return s