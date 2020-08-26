Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

* (A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

## Example 1:

![photo](https://assets.leetcode.com/uploads/2019/09/09/2whqcep.jpg)

* Input: [8,3,10,1,6,null,14,null,null,4,7,13]
* Output: 7
* Explanation: 
* We have various ancestor-node differences, some of which are given below :  
|8 - 3| = 5  
|3 - 7| = 4  
|8 - 1| = 7  
|10 - 13| = 3  
* Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

## Note:

* The number of nodes in the tree is between 2 and 5000.
* Each node will have value between 0 and 100000.

## [原題目連結點我](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)
	
## 我的心得:
* main.py
* DFS 紀錄每條到底的情形，然後分別從個別情形抽取最大 diff，從中選 max
* 不過此法若遇到太大的 tree 會很慢慢慢慢慢，因為這要用到很多 stack 和 list
------

* main1.py
* 直接 DFS 紀錄目前 max 和 min 是甚麼，並在走到最尾的時候直接將差值傳回來最大差值
* 此法效能比 main.py 好非常多( 92.12% )
