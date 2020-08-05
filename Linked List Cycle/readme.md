Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


## Example 1:

* Input: head = [3,2,0,-4], pos = 1
* Output: true
* Explanation: There is a cycle in the linked list, where tail connects to the second node.

![avatar](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

## Example 2:

* Input: head = [1,2], pos = 0
* Output: true
* Explanation: There is a cycle in the linked list, where tail connects to the first node.

![avatar](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

## Example 3:

* Input: head = [1], pos = -1
* Output: false
* Explanation: There is no cycle in the linked list.

![avatar](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

	
## 我的心得:
* 若整個 head 根本沒有東西，return False
* 若有 head，但卻沒有 head 的下一個，即表示一開始就沒有接續了，return False
* 接著就是 iterate 所有 nodes，走過的值都標示成 "HaSeXiStEd" ( has existed )
* 如果一直走著走著發現遇到了 "HaSeXiStEd"，即表示有環，return True

--------------

* main2.py 是 slow and fast pointer的實作法
* 須小心不要 iterate 到 None 的部分，只需判斷 fast pointer 即可，因為 fast pointer 走最快
* 若中途走到的 node 是相同( id )的話，則代表有環(因為永遠繞不出去)