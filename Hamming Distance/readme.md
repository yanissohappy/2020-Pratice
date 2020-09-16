The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

## Note:  
0 ≤ x, y < 231.

## Example:

	Input: x = 1, y = 4

	Output: 2

## Explanation:

	1   (0 0 0 1)
	4   (0 1 0 0)
		↑   ↑

* The above arrows point to positions where the corresponding bits are different.

## [原題目連結點我](https://leetcode.com/problems/hamming-distance/)

## 我的心得:
* main.py
* 先用 xor 就可以檢測 bit 不同之處了
* 在不斷 shift to right 以檢測有幾個1
-----

* 然後我在討論區看到這個很漂亮的寫法:
```python 
	return bin(x^y).count('1')
```
