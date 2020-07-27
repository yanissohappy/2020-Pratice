# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head
        
        while l1 and l2:
            if l1.val >= l2.val:
                # current.next = current = ListNode(l2.val) 這行等同於下一行
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next
            else:
                # current.next = current = ListNode(l1.val) 這行等同於下一行
                current.next = ListNode(l1.val)
                current = current.next                
                l1 = l1.next
        
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return head.next        