# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        carry = 0
        null_head = ListNode(None)
        dummy_head = null_head
        n = max(len(a),len(b))
        a = a + [0] * (n-len(a))
        b = b + [0] * (n-len(b))
        for i in range(n):
            s = a.pop(0)+b.pop(0)+carry
            if s<10:
                carry = 0
                dummy_head.next = ListNode(s)
                dummy_head = dummy_head.next
            else:
                carry = 1
                dummy_head.next = ListNode(s%10)
                dummy_head = dummy_head.next
        if carry == 1:
            dummy_head.next = ListNode(1)
            dummy_head = dummy_head.next
        return null_head.next
