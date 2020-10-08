Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

## Example 1:

	Input: nums = [2,2,1]
	Output: 1

## Example 2:

	Input: nums = [4,1,2,1,2]
	Output: 4

## Example 3:

	Input: nums = [1]
	Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

## [原題目連結點我](https://leetcode.com/problems/single-number/)

## 我的心得:
* main.py
* 先 sort 好，再兩個兩個分群，如果兩個兩個分群的結果是不一樣的話，那就是第一個東西是只有一次的 element
* 還要考慮最後的情形，如果到結束時都還沒有找到，則最後一個即為 happend only once