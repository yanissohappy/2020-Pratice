Given two strings s and t , write a function to determine if t is an anagram of s.

## Example 1:

	Input: s = "anagram", t = "nagaram"
	Output: true

## Example 2:

	Input: s = "rat", t = "car"
	Output: false

## Note:
* You may assume the string contains only lowercase alphabets.

## Follow up:
* What if the inputs contain unicode characters? How would you adapt your solution to such case?

## [原題目連結點我](https://leetcode.com/problems/valid-anagram/)
	
## 我的心得:
* main.py
* 放入字典，對照 s 的時候是加上相對應字母的個數，對照 t 的時候是減掉相對應字母的個數

-----
* main1.py
* 效能比 main.py 好
* 利用 ASCII 計算數值總和，但要小心有以下可能:
	1. `s = "a"` `t = "ab"`所以要檢查長度是否相等
	2. `s = "cc"` `t = "ab"`這樣 ASCII 總和會相同，但是內容物根本是不同的，所以要檢查 set 是否相等
	
-----
* 還有一個方法，直接如下即可:
```python
	return sorted(s) == sorted(t)
```
