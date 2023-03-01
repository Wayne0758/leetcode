"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        flag=1
        a=grid[0][0]
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]!=a:
                    flag=0
        mid=n/2
        topleft=[[grid[i][j] for j in range(mid)] for i in range(mid)]
        topRight=[[grid[i][j] for j in range(mid,n)] for i in range(mid)]
        bottomLeft=[[grid[i][j] for j in range(mid)] for i in range(mid,n)]
        bottomRight=[[grid[i][j] for j in range(mid,n)] for i in range(mid,n)]
        if flag==0:
            node=Node(True,False,self.construct(topleft),self.construct(topRight),self.construct(bottomLeft),self.construct(bottomRight))
        else:
            if a==1:
                node=Node(True,True,None,None,None,None)
            else:
                node=Node(False,True,None,None,None,None)
        return node
