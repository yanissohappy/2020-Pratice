Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

## Example 1:

* Input: [5,7]
* Output: 4
## Example 2:

* Input: [0,1]
* Output: 0

## [原題目連結點我](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
	
## 我的心得:
* main.py
* 即是找 longest common prefix 的 bit 變形版
* 推算要 left_shift 幾次( m 和 n 右移了幾次)，再用最後所得的 longest common prefix 左移該次數即可
------

* main1.py
* 因為 and 每次的結果都只會比兩者還小至多相等，所以只要用最大的那個數( n )不斷和該數 -1 做 and，再將此 and 的結果給最大的數
* 中間就可以跳過不必要的 and
* 如此不斷地 iteration，直到最大的數( n )小於原先最小的數( m )，就可以停止