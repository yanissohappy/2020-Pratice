Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

## Example 1:

	Input: [3,1,2,4]
	Output: [2,4,3,1]
	The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

## Note:

	1 <= A.length <= 5000
	0 <= A[i] <= 5000

## [原題目連結點我](https://leetcode.com/problems/sort-array-by-parity/)

## 我的心得:
* main.py
* 很直觀的方法，遇到偶數差前面，遇到奇數放後面
* 但這效能很不好，所以我要改進
----

* main1.py
* 用 left, right 指標來計算
* 要注意的是 left 必須 < right，因為每次都會交換，若 left > right，則原來應該是偶數的位置又會被交換到奇數，所以必須在這裡設為終點
----

* main.2py
* 用了另一種想法，但是跟 main1.py 大同小異
* 若前面遇到的是偶數，就直接 index + 1；若前面遇到奇數，那麼必須跟後面的奇數交換，所以要先走直到遇到偶數為止