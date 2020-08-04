Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

## Example 1:

* Input: [1,2,3]
* Output: [1,2,4]
* Explanation: The array represents the integer 123.
## Example 2:

* Input: [4,3,2,1]
* Output: [4,3,2,2]
* Explanation: The array represents the integer 4321.
	
## 我的心得:
* 從 list pop 出值
* pop 都是從最後一個出來的，正好可以直接乘上 weight (權值)
* 每個 pass 權值都會更新成原來10倍，也會將乘上 weight 的某個 digit 加進 sum 裡
* 最後將 sum + 1
* 再利用除法及餘數，將 sum + 1 一一插入要 return 的 list 裡(從最前面放)