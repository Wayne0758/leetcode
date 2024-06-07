# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1list=[]
        l2list=[]
        while l1:
            l1list.append(l1.val)
            l1 = l1.next
        while l2:
            l2list.append(l2.val)
            l2 = l2.next
        addnums = []
        tmp=0
        while l1list or l2list or tmp:
            val1 = l1list.pop(-1) if l1list else 0
            val2 = l2list.pop(-1) if l2list else 0
            a = val1 + val2 + tmp
            tmp = a//10
            addnums = [a%10]+addnums
        res = ListNode(addnums[0])
        pre = res
        for num in addnums[1:]:
            cur = ListNode(num)
            pre.next = cur
            pre = cur
        return res
