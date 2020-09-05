Given a non-empty array of integers, return the k most frequent elements.

## Example 1:

	Input: nums = [1,1,1,2,2,3], k = 2
	Output: [1,2]

## Example 2:

	Input: nums = [1], k = 1
	Output: [1]

## Note:

	You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
	Your algorithm's time complexity **must be better than O(n log n)**, where n is the array's size.
	It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
	You can return the answer in any order.

## [原題目連結點我](https://leetcode.com/problems/top-k-frequent-elements/)
	
## 我的心得:
* main.py
* 先用 dict 收集 distinct key
* 然後創建一個跟原 nums list 一樣大的 freq，所以在 dict value (出現頻率愈高)愈大的，就會被放在 freq 裡 index 愈大的位置
* 要小心有一種可能是`nums = [1,2] k = 1`，這種情形答案是`[1,2]`，代表說吾人所做的 freq 應該要存入這樣的情形`[[],[1,2]]`
* 因為題目說**must be better than O(n log n)**，所以任何排序都是不可能的，因此用空間換時間應是最好的方式

-------
* 還要研究一下其他的解法^^