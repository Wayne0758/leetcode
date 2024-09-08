# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        part_size = size//k
        num_exceed_part = size%k

        cur = head
        for i in range(k):
            new_part = ListNode(0)
            tail = new_part

            cur_size = part_size
            if num_exceed_part > 0:
                num_exceed_part -= 1
                cur_size += 1
            for j in range(cur_size):
                tail.next = ListNode(cur.val)
                tail = tail.next
                cur = cur.next
            res[i] = new_part.next
        return res
