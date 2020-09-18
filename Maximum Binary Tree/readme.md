Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

* Construct the maximum tree by the given array and output the root node of this tree.

## Example 1:

	Input: [3,2,1,6,0,5]
	Output: return the tree root node representing the following tree:

		  6
		/   \
	       3     5
		\    / 
		 2  0   
		   \
			1
		
## Note:
* The size of the given array will be in the range [1,1000].

## [原題目連結點我](https://leetcode.com/problems/maximum-binary-tree/)

## 我的心得:
* main.py
* 每次都用遞迴找左半跟右半的最大，然後接到上一個遞迴函式的 root 即可 
-----

* 但我還想知道有沒有更好的想法，晚點回來做
