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
* 要小心 s = "ab" , t = "aa" 的測資
* 所以在檢查的時候要雙向都要檢查，s -> t 以及 t -> s
* 以上述測資為例，a 對應 a，b 又對應 a，這樣變成多對一，是不可以的
* a 對應 b，b 又對應 a 是可以的，因為本質上就是一對一
