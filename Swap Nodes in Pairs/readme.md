Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

## Example:

	Given 1->2->3->4, you should return the list as 2->1->4->3.

## [原題目連結點我](https://leetcode.com/problems/swap-nodes-in-pairs/)

## 我的心得:
* main.py
* 注意會有 head等於`[]`的測資
* 創造一個 dummy node，這樣在最後 return 時就不會喪失原應該有的 head
* 用`first`和`second`標記所要交換的 nodes
* 交換過程思維:
	1. `second.next`要保留成`temp1`
	2. `second`要保留成`temp2`
	3. 將`second`替換成`first`
	4. 將`second.next`替換成`temp1`
	5. 再將`first`替換成最一開始的 second，也就是`temp2`
	6. 再將`first.next`替換成最一開始的 second.next，也就是`temp2`
	7. 最後再記得將上一輪所記錄的最後一點`lastone`的 next 替換成現在的`first`
	8. 記得走一次就是跨兩個 nodes