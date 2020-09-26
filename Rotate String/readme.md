We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

## Example 1:

	Input: A = 'abcde', B = 'cdeab'
	Output: true

## Example 2:

	Input: A = 'abcde', B = 'abced'
	Output: false

## Note:
* A and B will have length at most 100.

## [原題目連結點我](https://leetcode.com/problems/rotate-string)

## 我的心得:
* main.py
* 只要複製 A 接在原來 A 的後面，然後比對`新複製出來的 A`有沒有哪個片段(片段長即為 B 的片段長)及`B 的片段`完全相同即可
* 然後本題測資又有空字串，請小心檢驗
