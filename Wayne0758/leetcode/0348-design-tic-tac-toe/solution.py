class TicTacToe:

    def __init__(self, n: int):
        self.hashmaprow = defaultdict(lambda : defaultdict(list))
        self.hashmapcol = defaultdict(lambda : defaultdict(list))
        self.hashmapdia = defaultdict(list)
        self.hashmapcou = defaultdict(list)
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.hashmaprow[player][row].append(col)
        self.hashmapcol[player][col].append(row)
        if row==col:
            self.hashmapdia[player].append(row)
        if row+col==self.n-1:
            self.hashmapcou[player].append(row)
        if len(self.hashmaprow[player][row]) == self.n or len(self.hashmapcol[player][col]) == self.n or len(self.hashmapdia[player]) == self.n or len(self.hashmapcou[player]) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
