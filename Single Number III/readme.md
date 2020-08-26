Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

* Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

 

## Example 1:

	Input: nums = [1,2,1,3,2,5]
	Output: [3,5]
	Explanation:  [5, 3] is also a valid answer.
	
## Example 2:

	Input: nums = [-1,0]
	Output: [-1,0]

## Example 3:

	Input: nums = [0,1]
	Output: [1,0]
 

## Constraints:

	1 <= nums.length <= 30000
	 Each integer in nums will appear twice, only two integers will appear once.

## [原題目連結點我](https://leetcode.com/problems/single-number-iii/)
	
## 我的心得:
* main.py
* 用字典紀錄個數即可

------
* main1.py
* 此法利用 XOR
* list 全部 XOR 一遍後，會得到只有各一個的 XOR 值(因為數值相同的 XOR 結果會是 0，而 0 跟任何數字 XOR 都會為該數字)
* 再來找 XOR 的結果最近一位的 1 並存成 mask，意思是說若 XOR 的結果若為 10100，則會找到 100 的遮罩
* 為甚麼要這麼做呢？以 `[1,2,1,3,2,5]` 為例，3 ^ 5 == 6，化成 bit pattern 為`011 ^ 101 == 110`，**只有不一樣的 bit 再經過 XOR 後會呈現 1**
* 故只要找到這種遮罩，並且再重新與所有的數值做 XOR，一個與遮罩做有值(有值的相同兩數被歸納到此區的 XOR 值為 0)，一個做會為零(與遮罩做結果為零的相同兩數被歸納到此區的 XOR 值為 0)，即可得出獨立的一組解
