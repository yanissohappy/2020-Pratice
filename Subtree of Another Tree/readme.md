Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

## Example 1:

	Given tree s:

		 3
		/ \
	       4   5
	      / \
	     1   2
	Given tree t:
	   4 
	  / \
	 1   2
	Return true, because t has the same structure and node values with a subtree of s.
	 

## Example 2:

	Given tree s:

		 3
		/ \
	       4   5
	      / \
	     1   2
		/
	       0
	Given tree t:
	   4
	  / \
	 1   2
	Return false.

## [原題目連結點我](https://leetcode.com/problems/subtree-of-another-tree/)

## 我的心得:
* main.py
* 邏輯是: 遇到相同的，就搭配 t 子樹一一比對，若中途發現不對了，就不用再繼續比對 t，這個判斷由`def checkSubtree(self, s, t)`達成；若相同的話就一直找到底，若 s 和 t 都能找到底，就代表 t 是 s 的子樹
* 若遇到不同的就直接往下找，一定要 traverse 整棵樹一遍
