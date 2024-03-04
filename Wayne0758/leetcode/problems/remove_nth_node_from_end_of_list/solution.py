# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        head1 = head2 = head
        while head:
            size += 1
            head = head.next
        pivot = size-n
        if pivot == 0:
            return head1.next
        counter=1
        while head2:
            if counter == pivot:
                head2.next = head2.next.next
                return head1
            counter += 1
            head2 = head2.next