Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

## Example 1:

	Input: 16
	Output: true

## Example 2:

	Input: 5
	Output: false

## Follow up: 
* Could you solve it without loops/recursion?

## [原題目連結點我](https://leetcode.com/problems/power-of-four/)

## 我的心得:
* main.py
* `copy_num`是用來移的，因為必須保持`num`的乾淨
* 看一下`copy_num`右移移到 0 可以移幾次
* 然後再使用`ans_ref`，一開始設定為 1，目的是用這個 1 左移 count - 1 次(會是 count - 1 是因為在移`copy_num`時最後要變成 0 才會跳出迴圈的那步會多一次) 
* 最後檢查`num`有沒有和左移完的`ans_ref`相等，另外也要知道 count 是不是移了奇數次，因為只有奇數次的右移才會是正確的版本
* 如下，發現從右邊開始算過去 1 的位置都是奇數位，才會是 4 的 power 數
```
	1
	100
	10000
	1000000
	100000000
	10000000000
	1000000000000
	......
	and so on
```
-----

* 我看到討論區有一個[很聰明的做法](https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations):
```python
	def isPowerOfFour(self, num):
			return num != 0 and num & (num-1) == 0 and num & 1431655765 == num
```

* 其解釋如下:
```
	Consider the valid numbers within 32 bit, and turn them into binary form, they are:

	1
	100
	10000
	1000000
	100000000
	10000000000
	1000000000000
	100000000000000
	10000000000000000
	1000000000000000000
	100000000000000000000
	10000000000000000000000
	1000000000000000000000000
	100000000000000000000000000
	10000000000000000000000000000
	1000000000000000000000000000000	

	Any other number not it the list should be considered as invalid.
	So if you XOR them altogether, you will get a mask value, which is:

	1010101010101010101010101010101 (1431655765)
	
	Any number which is power of 4, it should be power of 2, I use num &(num-1) == 0 to make sure of that.
	Obviously 0 is not power of 4, I have to check it.
	and finally I need to check that if the number 'AND' the mask value is itself, to make sure it's in the list above.
```
