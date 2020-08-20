Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

* The binary search tree is guaranteed to have unique values.

 

## Example 1:

* Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
* Output: 32
## Example 2:

* Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
* Output: 23
 

## Note:

* The number of nodes in the tree is at most 10000.
* The final answer is guaranteed to be less than 2^31.

## [原題目連結點我](https://leetcode.com/problems/range-sum-of-bst/)
	
## 我的心得:
* main.py 
* 想清楚遞迴結構就好，但效能不好
-----
* main1.py
* 我忘記 BST 的定義了! 所以 main.py 的效能不好，只有 5X %
* BST ( binary search tree)定義:
	1. 以左邊節點 ( left node ) 作為根的子樹 ( sub-tree ) 的所有值都小於根節點 ( root )
	2. 以右邊節點 ( right node ) 作為根的子樹 ( sub-tree ) 的所有值都大於根節點 ( root )
	3. 任意節點 ( node ) 的左、右子樹也分別符合 BST 的定義
	4. 不存在任何鍵值 ( key/value ) 相等的節點。
* 緊抓著定義，就讓此程式比起 main.py 版本快了 40% 的人(此版本 faster than 91.07%)

