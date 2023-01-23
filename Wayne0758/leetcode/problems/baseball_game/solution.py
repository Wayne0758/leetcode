class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        a=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                a.append(a[-1]+a[-2])
            elif operations[i]=="C":
                a.pop()
            elif operations[i]=="D":
                a.append(a[-1]*2)
            else:
                a.append(int(operations[i]))
        return sum(a)