Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

## Example 1:

	Input: [3, 2, 1]

	Output: 1

	Explanation: The third maximum is 1.

## Example 2:

	Input: [1, 2]

	Output: 2

	Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

## Example 3:

	Input: [2, 2, 3, 1]

	Output: 1

	Explanation: Note that the third maximum here means the third maximum distinct number.
	Both numbers with value 2 are both considered as second maximum.

## [原題目連結點我](https://leetcode.com/problems/third-maximum-number/)

## 我的心得:
* main.py
* 題目說只能用 O(n)，故我用了三次迴圈分別尋找最大、次大、第三大，每次都是 O(n)
* 一開始`first, second, third`都要設為無限小
* 順序如下:
	1. first 就是找的數值要比其他全部都要大
	2. (first 已找完) second 就是比 first 小(一定要小於，不可以小於等於)，且比其他都要大
	3. (second 已找完) third 就是比 second 小(一定要小於，不可以小於等於)，且比其他都要大