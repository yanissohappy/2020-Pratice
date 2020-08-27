Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

* Return the answer in an array.

 

## Example 1:

	Input: nums = [8,1,2,2,3]
	Output: [4,0,1,1,3]
	Explanation: 
	For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
	For nums[1]=1 does not exist any smaller number than it.
	For nums[2]=2 there exist one smaller number than it (1). 
	For nums[3]=2 there exist one smaller number than it (1). 
	For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

## Example 2:

	Input: nums = [6,5,4,8]
	Output: [2,1,0,3]

## Example 3:

	Input: nums = [7,7,7,7]
	Output: [0,0,0,0]
 

## Constraints:

* 2 <= nums.length <= 500
* 0 <= nums[i] <= 100

## [原題目連結點我](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
	
## 我的心得:
* main.py
* 先 sort 好，然後用相對應的數字找標號就好!
* 不過此法效能不好，還是用空間換時間是比較好的方式(先建好一個 len 為 101 的 list，因為** 0 <= nums[i] <= 100 ** ，然後計算好小於某個數字的個數一一放進該 list 裡
* 最後再 output 進 return list 即可)
