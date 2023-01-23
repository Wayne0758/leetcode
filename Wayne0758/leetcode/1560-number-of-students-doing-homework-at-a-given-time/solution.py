class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        a=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime and queryTime<=endTime[i]:
                a+=1
        return a
