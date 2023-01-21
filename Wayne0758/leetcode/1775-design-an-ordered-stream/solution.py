class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.b = 0
        self.a = [None]*(n+1)
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        c=[]
        self.a[idKey-1]=value
        while self.a[self.b]!=None:
            c.append(self.a[self.b])
            self.b+=1
        return c
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
