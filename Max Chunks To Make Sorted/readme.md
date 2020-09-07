Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

* What is the most number of chunks we could have made?

## Example 1:

	Input: arr = [4,3,2,1,0]
	Output: 1
	Explanation:
	Splitting into two or more chunks will not return the required result.
	For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

## Example 2:

	Input: arr = [1,0,2,3,4]
	Output: 4
	Explanation:
	We can split into two chunks, such as [1, 0], [2, 3, 4].
	However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

## Note:

	arr will have length in range [1, 10].
	arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

## [原題目連結點我](https://leetcode.com/problems/max-chunks-to-make-sorted/)

## 我的心得:
* main.py
* 不斷地找到分割線，分割線到前一個分割線自動會變成一個區間(這件事情由 count++ 的計數達成)，因此只要找還沒有找到的最大值就好，不斷地畫分即可。
* 亦即，最應該 sort 好的序列應該長這樣`[0,1,2,3,4,5,6,7,8,9,....]`
* 以下為範例:
	`[0,1,3,4,2,5,6,8,7,9]`
	`0|1|342|5|6|87|9|`