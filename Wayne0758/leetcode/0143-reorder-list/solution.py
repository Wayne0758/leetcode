# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        cur = slow.next
        pre = None
        slow.next = None
        while cur:
            pre, pre.next, cur = cur, pre, cur.next
        slow.next = None
        while pre:
            t1 = head.next
            t2 = pre.next
            head.next = pre
            pre.next = t1
            head = t1
            pre = t2
