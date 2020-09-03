Given a square array of integers A, we want the minimum sum of a falling path through A.

* A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

## Example 1:

	Input: [[1,2,3],[4,5,6],[7,8,9]]
	Output: 12
	Explanation: 
	The possible falling paths are:
	[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
	[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
	[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
	The falling path with the smallest sum is [1,4,7], so the answer is 12.

 

## Constraints:

	1 <= A.length == A[0].length <= 100
	-100 <= A[i][j] <= 100

## [原題目連結點我](https://leetcode.com/problems/minimum-falling-path-sum/)
	
## 我的心得:
* main.py
* 我確定這個結果會是對的，但是 size 太大會 TLE
* 然後我偷看了一下討論區，發現要用 DP，但我還沒有點進去任何的看實際實作，明天再繼續 :-P
-----
* main1.py
* **待做**