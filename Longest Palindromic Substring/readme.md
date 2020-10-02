Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

## Example 1:

	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.

## Example 2:

	Input: "cbbd"
	Output: "bb"

## [原題目連結點我](https://leetcode.com/problems/longest-palindromic-substring/)

## 我的心得:
* main.py
* 很 brute force 的一一枚舉出現在的片段是否是`palindrome`以及`長度是目前最大`
* 但也很直覺地，這樣的做法會 TLE (的確也 TLE 了)
-----

* 