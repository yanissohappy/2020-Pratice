Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

* The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

* For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

## Example 1:

* Input: 5
* Output: 2
* Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
## Example 2:

* Input: 7
* Output: 0
* Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
## Example 3:

* Input: 10
* Output: 5
* Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

## Note:

* 0 <= N < 10^9
* This question is the same as 476: https://leetcode.com/problems/number-complement/

## [原題目連結點我](https://leetcode.com/problems/complement-of-base-10-integer/)
	
## 我的心得:
* main.py
* 利用 2^n - 1 - N 的方式完成 (2^n - 1 代表取得 1 補數)
* 不過此法因為不是直接操作 bit，會運用到 power，所以速度慢
-----
* main1.py
* 效能進步很多
* 做法就是看 N 的 bit 數為多少，然後同時求該 bit_num (我定義他為 bit 數有幾位，在 bit pattern 就會有幾個 1 )
* 在將之與原 N bit toggle(即用 XOR )即可