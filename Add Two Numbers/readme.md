You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Example:

	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	Explanation: 342 + 465 = 807.

## [原題目連結點我](https://leetcode.com/problems/add-two-numbers/)

## 我的心得:
* main.py
* 先把各節點的數值用 str 型態存取下來，再進行運算就會方便得多
* 之後把運算的結果 (int)，再轉換成 str，之後再一一將值串接點上即可