You are given a string s, return the number of segments in the string. 

A segment is defined to be a contiguous sequence of non-space characters.

 

## Example 1:

	Input: s = "Hello, my name is John"
	Output: 5
	Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

## Example 2:

	Input: s = "Hello"
	Output: 1

## Example 3:

	Input: s = "love live! mu'sic forever"
	Output: 4

## Example 4:

	Input: s = ""
	Output: 0
 

## Constraints:

	0 <= s.length <= 300
	s consists of lower-case and upper-case English letters, digits or one of the following characters "!@#$%^&*()_+-=',.:".
	The only space character in s is ' '.

## [原題目連結點我](https://leetcode.com/problems/number-of-segments-in-a-string/)

## 我的心得:
* main.py
* 要設一個 flag，判斷說現在在計算的是不是 string，所以當遇到非 white space 時，馬上就要開啟 flag，同時 segment 的計數也要加 1，之後就要繼續看是不是還在 string 裡(因為同一個 string 不須再 count++)
* 若遇到空白的時候要解鎖 flag
-----

* 還有另一個方法，直接使用 API，但是 main.py 我主要是要用自己的想法完成。
```python
class Solution(object):
	def countSegments(self, s):
		_list = s.strip(" ").split(" ")
		count = 0
		for ss in _list: # 因為如果測資的字串有"a     b"這種情形的話，用 split 會在新的 list 產生太多空字串，所以最後要重新計數一次
			if ss: count += 1               
		return count
```

-----

* 再另一個想法:
* 如果發現一個 letter 後面跟著一個 white space，就可以 +1
