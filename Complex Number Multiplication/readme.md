Given two strings representing two complex numbers.

* You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

## Example 1:

	Input: "1+1i", "1+1i"
	Output: "0+2i"
	Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

## Example 2:

	Input: "1+-1i", "1+-1i"
	Output: "0+-2i"
	Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

## Note:

* The input strings will not have extra blank.
* The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

## [原題目連結點我](https://leetcode.com/problems/complex-number-multiplication/)
	
## 我的心得:
* main.py
* 就把`a + bi`的 a 和 b 拆出來計算即可