class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.st = []
        self.size = maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.st)<self.size:
            self.st.append(x)
        return None
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.st)>0:
            return self.st.pop()
        else:
            return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(len(self.st)):
            if i<k:
                self.st[i]+=val
        return None
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
