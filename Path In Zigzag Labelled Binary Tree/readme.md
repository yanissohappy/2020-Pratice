In an infinite binary tree where every node has two children, the nodes are labelled in row order.

* In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

![a](https://assets.leetcode.com/uploads/2019/06/24/tree.png)

* Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

## Example 1:

	Input: label = 14
	Output: [1,3,4,14]

## Example 2:

	Input: label = 26
	Output: [1,2,6,10,26]
 

## Constraints:

	1 <= label <= 10^6

## [原題目連結點我](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)

## 我的心得:
* main.py
* 我的方法:
	1. 先將值都放好進 tree 這個 list 裡
	2. 然後再用 label 的值，用其 index 不斷求其父節點 index，直到求到 root 為止
	3. 求父節點 index 的計算方式為:

		floor((現在 index - 1) / 2) 
* 但是效能不好，因為這是 brute force