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
* 因為本題其實是 greedy，每次都只看下一步最佳，然後也有子結構可以擴展成整個結構，所以可以使用 dp
* 做到某個 row 時可以直接利用上個 row 的結果，再加上當下所在的 element，並比較哪個值最小，再 assign 給相對應的 dp 的位置
* 如此就可以完成
* 但我要特別說的地方是，因為我平常很喜歡用`dp = [[0] * n] * len(A[0])`這種方式設 list，殊不知跑測資的時候出現 WA，百思不得其解，把 dp 列出來看覺得長超怪
* 因為我明明只是設 dp 的其中一個元素，但為甚麼整個 col 都改到值了?
* 後來才知道為甚麼，[stackoverflow 的解說](https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly)
* 在使用`[x]*3`時，等同於`[x, x, x]`，也就是說有三個 reference 指向同一個 var，故之後設值的時候會整個 col 一起改
* 所以最好的設二為陣列的方式就是這樣:
```python
	[[1]*4 for _ in range(3)]
```
