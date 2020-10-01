# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        str1, str2 = "", ""
        while l1 and l2:
            str1 = str(l1.val) + str1
            str2 = str(l2.val) + str2
            l1 = l1.next
            l2 = l2.next
        while l1:
            str1 = str(l1.val) + str1
            l1 = l1.next
        while l2:
            str2 = str(l2.val) + str2
            l2 = l2.next
            
        rev = str(int(str1) + int(str2))
        dummy = ListNode(None)
        current = dummy
        for i in range(len(rev) - 1, -1, -1):
            node = ListNode(rev[i])
            current.next = node
            current = current.next
            
        return dummy.next
        