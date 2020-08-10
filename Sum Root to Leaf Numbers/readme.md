Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

* An example is the root-to-leaf path 1->2->3 which represents the number 123.

* Find the total sum of all root-to-leaf numbers.

* Note: A leaf is a node with no children.

## Example:

* Input: [1,2,3]  
　　　1  
　　/　 \  
　2　　　3  
* Output: 25
## Explanation:
The root-to-leaf path 1->2 represents the number 12.  
The root-to-leaf path 1->3 represents the number 13.  
Therefore, sum = 12 + 13 = 25.  
## Example 2:

* Input: [4,9,0,5,1]  
　　　　4  
　　　/　　\  
　　9　　　　0  
　/　　　　　\  
5　　　　　　　1  
* Output: 1026  
* Explanation:  
The root-to-leaf path 4->9->5 represents the number 495.  
The root-to-leaf path 4->9->1 represents the number 491.  
The root-to-leaf path 4->0 represents the number 40.  
Therefore, sum = 495 + 491 + 40 = 1026.  

## [原題目連結點我](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
	
## 我的心得:
* 小!心!沒!有! node !的!情!況!
* 所有最後到底的數值都會存進 list，sum 只要 return 該 list 的每個元素的值就好
---------------

* 法二：利用 left shift 和 right shift，再各自相加，即可不斷得到下一排
