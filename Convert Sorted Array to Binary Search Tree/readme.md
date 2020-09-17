Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

## Example:

	Given the sorted array: [-10,-3,0,5,9],

	One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

		  0
		 / \
	   -3   9
	   /   /
	 -10  5

## [原題目連結點我](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## 我的心得:
* main.py
* 因為 list 已經排序好，所以每次都只要找尋 list 的正中間，然後製作成一個節點，並且在左子節點和右子節點分別接上`遞迴下去的 list 左半邊的正中間的數值`以及`遞迴下去的 list 右半邊的正中間的數值`即可