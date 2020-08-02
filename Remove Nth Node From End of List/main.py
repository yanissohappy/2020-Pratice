# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        current = head
        while current != None:
            length += 1
            current = current.next
        destination = length - n - 1
        counter = 0
        current = head
        if destination == -1: # means remove the first node
            return head.next
        while counter != destination:
            counter += 1
            current = current.next
        # find the node
        if n == 1: # if it is the last one
            current.next = None        
        else:
            current.next = current.next.next
            
        return head
            