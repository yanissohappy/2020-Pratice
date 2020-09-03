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