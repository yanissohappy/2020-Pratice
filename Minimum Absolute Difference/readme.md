Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

* Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

*a, b are from arr
*a < b
*b - a equals to the minimum absolute difference of any two elements in arr
 

## Example 1:

	Input: arr = [4,2,1,3]
	Output: [[1,2],[2,3],[3,4]]
	Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

## Example 2:

	Input: arr = [1,3,6,10,15]
	Output: [[1,3]]
	
## Example 3:

	Input: arr = [3,8,-10,23,19,-4,-14,27]
	Output: [[-14,-10],[19,23],[23,27]]
 

## Constraints:

* 2 <= arr.length <= 10^5

## [原題目連結點我](https://leetcode.com/problems/minimum-absolute-difference/)
	
## 我的心得:
* main.py
* 先 sort 好，找每每兩個的差值的最小值
* 找到後，再比對一次，若差值能夠達到此最小值，則 output 在 return list 裡