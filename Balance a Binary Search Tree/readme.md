Given a binary search tree, return a balanced binary search tree with the same node values.

* A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

* If there is more than one answer, return any of them.

 

## Example 1:

![photo](https://assets.leetcode.com/uploads/2019/08/22/1515_ex1.png)
![photo](https://assets.leetcode.com/uploads/2019/08/22/1515_ex1_out.png)

* Input: root = [1,null,2,null,3,null,4,null,null]
* Output: [2,1,3,null,null,null,4]
* Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

## Constraints:

* The number of nodes in the tree is between 1 and 10^4.
* The tree nodes will have distinct values between 1 and 10^5.

## [原題目連結點我](https://leetcode.com/problems/balance-a-binary-search-tree/)
	
## 我的心得:
* main.py
* DFS，然後用取得的值(會是由小到大的)製作一棵  balanced binary search tree (每次都從中間砍半接)