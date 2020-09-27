You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Example 1:

	Input: 2
	Output: 2
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps

## Example 2:

	Input: 3
	Output: 3
	Explanation: There are three ways to climb to the top.
	1. 1 step + 1 step + 1 step
	2. 1 step + 2 steps
	3. 2 steps + 1 step

## Constraints:

* 1 <= n <= 45

## [原題目連結點我](https://leetcode.com/problems/climbing-stairs/)

## 我的心得:
* main.py
* 很直覺的遞迴作法，但是做到`n == 38`時就會 TLE
-----
* main1.py
* 我看討論區的思路，這題其實是 Fibonacci 數
* 想法是: 現在要求`n`，因為題目限制每次都只能走 1 或 2 步，代表`n`一定是由`n-1`和`n-2`來的
* 而`n-1`是由`n-2`和`n-3`(if exists)來的...類似的思考至底
* 所以我們可以做一個`step` list，用 Bottom up 的方式組出答案，最終就能以線性時間去計算出最終結果