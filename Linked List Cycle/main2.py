# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next or not head.next.next:
            return False
        slow_pointer, fast_pointer = head.next, head.next.next
        while fast_pointer != None:
            if fast_pointer == slow_pointer:
                return True
            if fast_pointer and fast_pointer.next and fast_pointer.next.next:
                slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
            else:
                return False
        return False