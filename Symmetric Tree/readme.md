Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

* For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1  
   / \  
  2   2  
 / \ / \  
3  4 4  3  
 

* But the following [1,2,2,null,3,null,3] is not:

    1  
   / \  
  2   2  
   \   \  
   3    3  

## [原題目連結點我](https://leetcode.com/problems/symmetric-tree/)
	
## 我的心得:
* 這題只要做兩個DFS，一個是 left to right，一個是 right to left，然後分別放進 list 裡面( null 值也要塞進去!我是用 None 塞的)
* 然後再比對這兩個 list 是否相同即可