Given a linked list, remove the n-th node from the end of list and return its head.

## Example:

* Given linked list: 1->2->3->4->5, and n = 2.

* After removing the second node from the end, the linked list becomes 1->2->3->5.
## Note:

* Given n will always be valid.

## Follow up:

* Could you do this in one pass?
	
## 我的心得:
* 要數過一遍 list 的長度為何，再計算 n 所代表的 node 的"前一點"的 index
* list 的問題都要考慮首、中間、尾
* 若是要移除首的時候直接 return 原來頭的下一個就好
* 而中間的部分，用最上面所說的 index 來處理，因為都是"要刪除的 node 的前一點"，所以該點的 next 會處理成"原來 next 的 next"
* 若是移除最末的部分，只要將"要刪除的 node 的前一點的next"設為 None 即可(在 C語言 中是處理成 Null)
* list 若 iterate 沒有做好(比如說超出list範圍，某點都已經 None 了還要求 next)容易出現 AttributeError: 'NoneType' object has no attribute 'next' 的錯誤訊息