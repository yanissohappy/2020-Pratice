We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

* Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

* (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

## Example 1:

	Input: [1,null,0,0,1]
	Output: [1,null,0,null,1]
	 
	Explanation: 
	Only the red nodes satisfy the property "every subtree not containing a 1".
	The diagram on the right represents the answer.

![p](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

## Example 2:

	Input: [1,0,1,0,0,0,1]
	Output: [1,null,1,null,1]

![p](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

## Example 3:

	Input: [1,1,0,1,1,0,1,0]
	Output: [1,1,0,1,1,null,1]

![p](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

## Note:

	The binary tree will have at most 200 nodes.
	The value of each node will only be 0 or 1.

## [原題目連結點我](https://leetcode.com/problems/binary-tree-pruning/)
	
## 我的心得:
* main.py
* 要想好怎麼接點!!!!!!!!!!
