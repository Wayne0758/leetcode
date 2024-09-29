class TextEditor:

    def __init__(self):
        self.s = '|'
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.s = self.s[:self.cursor]+text+self.s[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        newcursor = max(self.cursor-k,0)
        k = self.cursor - newcursor
        self.s = self.s[:self.cursor-k]+self.s[self.cursor:]
        self.cursor -= k
        return k

    def cursorLeft(self, k: int) -> str:
        newcursor = max(self.cursor-k,0)
        k = self.cursor - newcursor
        self.cursor = newcursor
        self.s = self.s[:self.cursor] + '|' + self.s[self.cursor:self.cursor+k] + self.s[self.cursor+k+1:]
        return self.s[self.cursor-min(10,self.cursor):self.cursor]

    def cursorRight(self, k: int) -> str:
        newcursor = min(self.cursor+k,len(self.s)-1)
        k = newcursor - self.cursor
        self.cursor = newcursor
        self.s = self.s[:self.cursor-k] + self.s[self.cursor-k+1:self.cursor+1] +'|'+ self.s[self.cursor+1:]
        return self.s[self.cursor-min(10,self.cursor):self.cursor]
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
