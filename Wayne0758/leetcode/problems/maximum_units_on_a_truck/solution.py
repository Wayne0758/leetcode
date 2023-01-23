class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda x:-x[1])
        a=0
        for i in range(len(boxTypes)):
            if truckSize > boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                a += boxTypes[i][0]*boxTypes[i][1]
            else:
                a += truckSize*boxTypes[i][1]
                break
        return a