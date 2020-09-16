Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

## Example:

	Input: [0,1,0,3,12]
	Output: [1,3,12,0,0]
	
## Note:

	You must do this in-place without making a copy of the array.
	Minimize the total number of operations.

## [原題目連結點我](https://leetcode.com/problems/move-zeroes/)

## 我的心得:
* main.py
* 遇到非零數一律左移，並且計算現在遇到多少非零數
* 我取名為 how_many_zero 的用意是，最後結束計數非零的數值的 index 之後到原 nums 的長度為止都要設為 0
------
* main1.py
* 有使用到 del 的超直覺作法，但 del 是`O(n)`的作法，所以包在迴圈內的 worst case 是 O(n ^ 2) (如果全部都是`[0,0,0,0,0,....,0]`，每遇到`0`就要不停拔掉)