Given an array of integers arr, replace each element with its rank.

* The rank represents how large the element is. The rank has the following rules:

* Rank is an integer starting from 1.
* The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
* Rank should be as small as possible.
 

## Example 1:

	Input: arr = [40,10,20,30]
	Output: [4,1,2,3]
	Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

## Example 2:

	Input: arr = [100,100,100]
	Output: [1,1,1]
	Explanation: Same elements share the same rank.

## Example 3:

	Input: arr = [37,12,28,9,100,56,80,5,12]
	Output: [5,3,4,2,8,6,7,1,3]
 

## Constraints:

	0 <= arr.length <= 10^5
	-10^9 <= arr[i] <= 10^9

## [原題目連結點我](https://leetcode.com/problems/rank-transform-of-an-array/)
	
## 我的心得:
* main.py
* 好久沒練習一般的 sort，這次選用時間複雜度不太好的 bubble sort (我還是要熟悉這是怎麼做的)
* 但是 leetcode 有一筆超大的測資([bigdata.txt](./bigdata.txt))，我的方法是不斷地用 indexOf 來找，這樣會使得時間變很差，為O(n^2)
-----

* main1.py
* 改良版是直接使用字典和 set