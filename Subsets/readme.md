Given a set of distinct integers, nums, return all possible subsets (the power set).

* Note: The solution set must not contain duplicate subsets.

## Example:

	Input: nums = [1,2,3]
	Output:
	[
	  [3],
	  [1],
	  [2],
	  [1,2,3],
	  [1,3],
	  [2,3],
	  [1,2],
	  []
	]

## [原題目連結點我](https://leetcode.com/problems/subsets/)
	
## 我的心得:
* main.py
* 這題是 DFS 的應用
* temp 每次塞完給下一次 DFS 後都記得要拔掉，因為要保持同一層的最初的初始值
-----

* 然後我在討論區看到超厲害的解法，茲紀錄:

```python
	class Solution(object):
		def subsets(self, nums):
			nums.sort()
			result = [[]]
			for num in nums:
				result += [i + [num] for i in result]
			return result
```
* 有點難讀懂，拆解成下面:
```python
	class Solution:
		def subsets(self, nums):
			result = [[]]
			for number in nums:
				for i in result:
					# append (i in result list + number) to result list
					result = result + [i + [number]]
			return result
```
* i 的東西都會是這樣的形式`[]`,`[1]`,[1,2,4]`...
* 所以`i + [number]`比如說就是`[1] + [number]`，所以最後結果也會是一個`[1, number...]`
* 最後`result + [i + [number]]`的`[i + [number]]`就是把`[1, number...]`這整塊東西放入`result`裡
* 加入的過程如下，以`[1,2,3]為例`:

	('result:', [[]])
	('result:', [[], [1]])
	('result:', [[], [1], [2]])
	('result:', [[], [1], [2], [1, 2]])
	('result:', [[], [1], [2], [1, 2], [3]])
	('result:', [[], [1], [2], [1, 2], [3], [1, 3]])
	('result:', [[], [1], [2], [1, 2], [3], [1, 3], [2, 3]])