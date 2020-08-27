Given a collection of distinct integers, return all possible permutations.

Example:

	Input: [1,2,3]
	Output:
	[
	  [1,2,3],
	  [1,3,2],
	  [2,1,3],
	  [2,3,1],
	  [3,1,2],
	  [3,2,1]
	]

## [原題目連結點我](https://leetcode.com/problems/permutations/)
	
## 我的心得:
* main.py
* 每次 recursive 都選取一個 element 作為 victim
* 接下來就繼續用剩下的就是排除該 element 的其他元素，不斷地選 victim，直到 remaining 的部分為空為止
* 要注意 pass by reference 的 issue