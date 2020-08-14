Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

* We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

## Example 1:

* Input: nums = [4,2,3]
* Output: true
* Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
## Example 2:

* Input: nums = [4,2,1]
* Output: false
* Explanation: You can't get a non-decreasing array by modify at most one element.
 

## Constraints:

* 1 <= n <= 10 ^ 4
* - 10 ^ 5 <= nums[i] <= 10 ^ 5

## [原題目連結點我](https://leetcode.com/problems/non-decreasing-array/)
	
## 我的心得:
* 這題卡了有點久，寫出來不難但是很多情況要考慮清楚
* 比較容易有問題的測資，這幾種都測過應該就沒有問題:
		[2,3,3,2,4]  
		[4,2,3]  
		[3,2,2,3]  
		[3,4,2,3]  
* 若 num[5] > num[6]，會有兩種情形，一是將 num[5] 的值改成 num[6]，不然就是將 num[6] 的值改成 num[5]
* 因為前面都檢查過了可以保證是 non-decreasing，但 num[5] 的值改成 num[6] 必須檢查 num[6] 的值是否大於 num[4] (即 index 6 的前兩個)，若沒有大於，則將 num[6] 的值改成 num[5]  