Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

## Example 1:


	Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
	Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

## Constraints:

	m == mat.length
	n == mat[i].length
	1 <= m, n <= 100
	1 <= mat[i][j] <= 100

## [原題目連結點我](https://leetcode.com/problems/sort-the-matrix-diagonally/)

## 我的心得:
* main.py
* 只要都從最左邊，最上邊出發不斷地往右下跑到底就好，跑到底的`temp_list`sort 完之後就要 pop(0) 回去一一填入