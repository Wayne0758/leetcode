# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head=head.next
        resnums = []
        for i in range(0, len(nums), 2):
            revval=nums[i:i+2]
            resnums +=revval[::-1]
        print(resnums)
        res = ListNode(0)
        cur = res
        for num in resnums:
            cur.next = ListNode(num)
            cur = cur.next
        return res.next
