# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        if not head.next:
            return False
        while head and head.next:
            if head.val == "HaSeXiStEd":
                return True
            head.val = "HaSeXiStEd"
            head = head.next
        