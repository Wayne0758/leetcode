# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, pre: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = pre.next
        cur = start.next
        after = start
        for i in range(n-1):
            start.next, cur.next, pre.next= cur.next, pre.next, cur
            cur = start.next
        return after

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        revcur = None
        count=0
        i=1
        while cur:
            count += 1
            if count == i or cur.next==None:
                if count%2==0:
                    cur = self.rev(revcur, count)
                revcur = cur
                i += 1
                count = 0
            cur = cur.next
        return head
