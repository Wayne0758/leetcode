class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        a='MGP'
        s=0
        for i in range(len(a)):
            flag=0
            end=0
            for j in range(len(garbage)):
                while a[i] in garbage[j]:
                    garbage[j]=garbage[j].replace(a[i],'',1)
                    s+=1
                    end=j
            b=travel[:end]
            s+=sum(b)
        return s
