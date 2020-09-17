Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

* For example:  
Given binary tree [3,9,20,null,null,15,7],  

		3
	   / \
	  9  20
		/  \
	   15   7
	   
return its bottom-up level order traversal as:  

	[
	  [15,7],
	  [9,20],
	  [3]
	]

## [原題目連結點我](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

## 我的心得:
* main.py
* 用 BFS 的概念
* 解釋: 先找好整棵樹最深的深度，然後用此深度建立相對應的 list of list，並也要視現在在哪一層放入值
* 用此方式就可以倒著放，所以參數中的 level 會慢慢遞減，功用是為了在相對應的 list 放入值
* 放值方式依舊是由左到右，所以遞迴也是先 left node，再 right node

----

* main1.py
* 我一開始想到的最直接的方式就是 BFS，然後最終結果再 reverse
* 但這個效能不是很好