# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        pre_head = head
        while pre_head:
            l.append(pre_head.val)
            pre_head = pre_head.next
        l = sorted(l)
        dummyHead = ListNode(0)
        tail = dummyHead
        for i in l:
            tail.next = ListNode(i)
            tail = tail.next
        return dummyHead.next
