class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        a=[]
        b=[]
        for i in range(len(groupSizes)):
            flag=0
            for j in range(len(a)):
                if len(a[j])==groupSizes[i]:
                    flag=1
                    for k in range(len(a[j])):
                        if a[j][k] == None:
                            a[j][k]=i
                            break
                    if a[j][-1] != None:
                        b.append(a[j])
                        a.remove(a[j])
                        break
            if flag==0:
                if groupSizes[i]==1:
                    b.append([i])
                else:
                    a.append([i]+[None for k in range(groupSizes[i]-1)])
        return b