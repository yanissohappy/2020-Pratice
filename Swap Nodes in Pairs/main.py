# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head
        dummy = ListNode(None)
        lastone, first, second = dummy, head, head.next
        if not second:
            return head
        
        while first != None and second != None:
            temp1 = second.next
            temp2 = second
            second = first
            second.next = temp1
            first = temp2
            first.next = second
            lastone.next = first                       
            
            if lastone.next.next and first.next.next and second.next.next : 
                lastone = lastone.next.next
                first = first.next.next
                second = second.next.next
            else:
                break
        
        return dummy.next