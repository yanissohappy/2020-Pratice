Reverse a singly linked list.

## Example:

	Input: 1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL

## Follow up:

* A linked list can be reversed either iteratively or recursively. Could you implement both?

## [原題目連結點我](https://leetcode.com/problems/reverse-linked-list/)
	
## 我的心得:
* main.py
* 從頭開始拔，並且一一塞給新的( prev ) linked list
* 要注意的是一拔完(一 assign 給 curr)，原 head 就要馬上指給下一個以截斷