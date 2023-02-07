# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        a=[[-1 for j in range(n)] for i in range(m)]
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        i=0
        j=0
        d=0
        while head:
            a[i][j]=head.val
            head=head.next
            nexti,nextj=i+dir[d][0],j+dir[d][1]
            if nexti==m or nextj==n or a[nexti][nextj] != -1:
                d=(d+1)%4
            i,j=i+dir[d][0],j+dir[d][1]
        return a

