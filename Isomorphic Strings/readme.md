Given two strings s and t, determine if they are isomorphic.

* Two strings are isomorphic if the characters in s can be replaced to get t.

* All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

## Example 1:

* Input: s = "egg", t = "add"
* Output: true
## Example 2:

* Input: s = "foo", t = "bar"
* Output: false
## Example 3:

* Input: s = "paper", t = "title"
* Output: true
## Note:
* You may assume both s and t have the same length.

## [原題目連結點我](https://leetcode.com/problems/isomorphic-strings/)
	
## 我的心得:
* main.py
* 這個在 s = "ab" , t = "aa" 的測資時會錯
* 太累了先 commit，睡醒改 