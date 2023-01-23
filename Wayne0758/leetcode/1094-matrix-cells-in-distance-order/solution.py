class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(rows):
            for j in range(cols):
                a.append([i,j])
        a.sort(key = lambda x:abs(rCenter-x[0])+abs(cCenter-x[1]))
        return a
