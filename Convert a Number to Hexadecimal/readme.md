Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

## Note:

* All letters in hexadecimal (a-f) must be in lowercase.
* The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
* The given number is guaranteed to fit within the range of a 32-bit signed integer.
* You must not use any method provided by the library which converts/formats the number to hex directly.
## Example 1:

* Input:  
26

* Output:
"1a"  
## Example 2:

* Input:  
-1

* Output:  
"ffffffff"

## [原題目連結點我](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)
	
## 我的心得:
* 分成三種情形， >0 , ==0 , <0 ，並且有相對應的處理
* 不斷得到餘數，並且判斷該餘數在 return 的字串的值為何
* 在數值為負數的部分，要先轉成正值，再 1's C 再加 1，此時此值即為負數，再用上條的方法不斷 iteration 即可得出最終結果
-----

* 我在討論區看到一個很聰明的方法，特此紀錄:
				''.join(
							'0123456789abcdef'[(num >> 4 * i) & 15] 
							for i in range(8)
							)[::-1].lstrip('0') or '0'

* 該法即為不斷從 '0123456789abcdef' 選出相對應的位置(所以就不用像我一樣寫函式)
* "& 15" 即為 %16 之意!!!(我覺得很巧妙!! 此人很精通 bit 操作!) 