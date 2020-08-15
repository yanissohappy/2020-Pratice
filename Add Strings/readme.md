Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

## Note:

* The length of both num1 and num2 is < 5100.
* Both num1 and num2 contains only digits 0-9.
* Both num1 and num2 does not contain any leading zero.
* You must not use any built-in BigInteger library or convert the inputs to integer directly.

## [原題目連結點我](https://leetcode.com/problems/add-strings/)
	
## 我的心得:
* main.py
* Brute force
-------

* main1.py
* 利用 ord 和 chr，以及搭配簡單的單位加法，需要考量 carry
* 在 iteration 做完時要檢查最後 carry 是不是還有值，有的話代表最後有進位，必須塞 1 在前面
* 此法比 main.py 效能好很多