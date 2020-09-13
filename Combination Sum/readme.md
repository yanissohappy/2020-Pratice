Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

## Note:

	All numbers (including target) will be positive integers.
	The solution set must not contain duplicate combinations.

## Example 1:

	Input: candidates = [2,3,6,7], target = 7,
	A solution set is:
	[
	  [7],
	  [2,2,3]
	]

## Example 2:

	Input: candidates = [2,3,5], target = 8,
	A solution set is:
	[
	  [2,2,2,2],
	  [2,3,3],
	  [3,5]
	]
	 

## Constraints:

	1 <= candidates.length <= 30
	1 <= candidates[i] <= 200
	Each element of candidate is unique.
	1 <= target <= 500

## [原題目連結點我](https://leetcode.com/problems/combination-sum/)

## 我的心得:
* main.py
* 每次都只能對當下所處理的 list 的 index 及其之後的 index (不能對之前!)做處理，就可以完成 combination 的要求(就不會出現排列)，但用此方法需先將 candidate sort 好
* 不然這次的正解順序也會考慮進去
* 比如說，`[3,4,5,6]`放進 recursive 函式裡，當第一次 loop 選定 3 後，就會傳入 index 0 給下一次 recursion，說明下一次 recursion 從 index 0 開始；而第二次 loop 會選定 4，就會傳入 index 1 給下一次 recursion，說明下一次 recursion 從 index 1 開始，是這樣才可以保證只會有組合的出現，而非排列
