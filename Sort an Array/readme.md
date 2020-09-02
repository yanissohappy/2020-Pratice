Given an array of integers nums, sort the array in ascending order.

 

## Example 1:

	Input: nums = [5,2,3,1]
	Output: [1,2,3,5]

## Example 2:

	Input: nums = [5,1,1,2,0,0]
	Output: [0,0,1,1,2,5]
	 

## Constraints:

* 1 <= nums.length <= 50000
* -50000 <= nums[i] <= 50000

## [原題目連結點我](https://leetcode.com/problems/sort-an-array/)
	
## 我的心得:
* main.py
* 使用 merge sort
* merge sort 演算法乃用 recursive，不斷地切切切，切到只剩一個為止，然後 return 後就可以開始 merge 所 return 的東西
* merge 的方法是都是用兩個 list 的第一個 element 來進行比較，小於的話就把他抓出來，放到要 return 的 list 裡，不斷抓，直到抓完為止
* 然後我發現如果 output 太多行數也會出錯... (Output Limit Exceeded) 所以 Debug 完也要記得把 print 刪除
