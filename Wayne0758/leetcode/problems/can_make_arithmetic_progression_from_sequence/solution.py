class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        flag=True
        dif=arr[1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]!=dif:
                flag=False
        return flag