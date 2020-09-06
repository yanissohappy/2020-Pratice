Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

## Note:
* The array size can be very large. Solution that uses too much extra space will not pass the judge.

## Example:

	int[] nums = new int[] {1,2,3,3,3};
	Solution solution = new Solution(nums);

	// pick(3) should return either index 2, 3, or 4 randomly. Each index should have **equal probability** of returning.
	solution.pick(3);

	// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
	solution.pick(1);

## [原題目連結點我](https://leetcode.com/problems/random-pick-index/)

## 我的心得:
* main.py
* 此題很直觀的解法就是會用到 random，因為 random 確實是 [0.0~1.0) 出現機率會相同的
* 但是假如說有一種情形，當一個 array 是`[3,3,3,3,3,3]`，然後測資欲短時間快速`pick(3)`，用此法就只會 output 出相同的 index
* 所以上面的方法被我註解掉了，然後我新增一個 dictionary，去標記現在在做的那個數值現在處於另外一個 dictionary 的 list 中的哪一個 index，有一點拗口，仔細研讀 code 就可以理解的
* 因此也要計算當下所處的 index 有沒有等於`_dict[數字]`的長度，若有，則要重新從 0 開始計數
* 此法亦可保證 equal probability