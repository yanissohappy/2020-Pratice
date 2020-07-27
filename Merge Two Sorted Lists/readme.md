Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

## Example:

* Input: 1->2->4, 1->3->4
* Output: 1->1->2->3->4->4

## 我的心得:

    current.next = current = ListNode(l2.val)
這行等同於

    current.next = ListNode(l2.val) # 目的是新construct的接給目前node的下一個 
    current = current.next #目的是將目前node所指的換指下一個，之後才可以很好的串接

也就是說，最右方的會一一assign給從最左方開始的每一個東西，直到最右方的前一個
