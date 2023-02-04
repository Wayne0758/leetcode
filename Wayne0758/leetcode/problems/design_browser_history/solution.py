class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.st=[homepage]
        self.cnt=0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.st=self.st[:self.cnt+1]
        self.st.append(url)
        self.cnt+=1
        return None

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.cnt>steps:
            self.cnt-=steps
        else:
            self.cnt=0
        return self.st[self.cnt]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.cnt+steps<len(self.st):
            self.cnt+=steps
        else:
            self.cnt=len(self.st)-1
        return self.st[self.cnt]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)