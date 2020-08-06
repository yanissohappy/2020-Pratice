Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

## For example:
* Given binary tree [3,9,20,null,null,15,7]
* 
    3
   / \
  9  20
    /  \
   15   7
* return its level order traversal as:
* 
[
  [3],
  [9,20],
  [15,7]
]

## [原題目連結點我](https://leetcode.com/problems/binary-tree-level-order-traversal/)
	
## 我的心得:
* 這題我的寫法比較生吞活剝
* 首先建立 dict，為的是得知每一層有多少非 null 的 node
* dict 建立完後，就可以 traverse node
* 方法是使用 list ( queue )，因為這題的概念是 BFS，剛好跟 queue FIFO 的特性相同
* 每一次 iteration 都要查該層的 node 有幾個，然後比對現在做到幾個 node
* 要非常小心" 一顆 node 都沒有 "的情形
* 但我想我一定有多考慮甚麼不必要的東西，所以我還會繼續思考這題
* Reminder : null 的下面不會有東西了，所以他的下面不會還有 null 這種東西，我一直以為原 root 只要沒有都會塞 null。這是我卡很久的盲點 :( 
