class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        arr.append(None)
        a=[]
        x=arr[0]
        y=1
        for i in range(1,len(arr)):
            if arr[i]==x:
                y+=1
            else:
                if y in a:
                    return False
                else:
                    a.append(y)
                x=arr[i]
                y=1
        return True