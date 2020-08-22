Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

* Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

* For example,   

Given the tree:  
	　　　　4  
	　　　/　\  
	　　2　　7  
	　/　\  
	1　　3  
And the value to insert: 5  
You can return this binary search tree:  

	　　　　4  
	　　　/　\  
	　　2　　7  
	　/　\　/  
	1　　3　5  
This tree is also valid:  

	　　　　　5  
	　　　　/　\  
	　　　2　　7  
	　　/　\     
	　1　　3  
	　　　　\  
	　　　　　4  
 

## Constraints:

* The number of nodes in the given tree will be between 0 and 10^4.
* Each node will have a unique integer value from 0 to -10^8, inclusive.
* -10^8 <= val <= 10^8
* It's guaranteed that val does not exist in the original BST.

## [原題目連結點我](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
	
## 我的心得:
* main.py
* 就是不斷找到底，然後插入即可
-----
* main1.py
* 是 main.py 的詳細版，但是因為每一步都會多檢查下一個 node 有沒有 None，所以效能差 
* 注意 main.py 和 main1.py 的差異:
```python
        if not root:
            return TreeNode(val)
```
* 在上面這段程式碼中兩者代表的意義不同，main.py 是從最後面開始；而 main1.py 則是避免掉空樹的狀況，所以兩者皆不可省略