Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

* You may return the answer in any order.

 

## Example 1:

	Input: n = 4, k = 2
	Output:
	[
	  [2,4],
	  [3,4],
	  [2,3],
	  [1,2],
	  [1,3],
	  [1,4],
	]
	
## Example 2:

	Input: n = 1, k = 1
	Output: [[1]]
 

## Constraints:

	1 <= n <= 20
	1 <= k <= n

## [原題目連結點我](https://leetcode.com/problems/combinations/)

## 我的心得:
* main.py
* 一樣是先前所練習過的 combination 的變形版，惟要記得的 temp 在 append 完之後要 pop 掉，才能保持當下在迴圈的乾淨度