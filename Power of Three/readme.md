Given an integer, write a function to determine if it is a power of three.

## Example 1:

	Input: 27
	Output: true

## Example 2:

	Input: 0
	Output: false

## Example 3:

	Input: 9
	Output: true

## Example 4:

	Input: 45
	Output: false

## Follow up:
* Could you do it without using any loop / recursion?

## [原題目連結點我](https://leetcode.com/problems/power-of-three/)
	
## 我的心得:
* main.py
* 三的倍數可以直接用 3 ** x 的方式判斷，但我覺得這樣會比較慢，還是用 bit 左移一次 再加上 原來的數(即為 2*x + x = 3 * x)即可。
------

* 題目說有辦法不用 loop，我去看討論區，是直接用 3^19 % n 就好 (因為 int 的最大值小於 3^20)

```java
public class Solution {
public boolean isPowerOfThree(int n) {
    // 1162261467 is 3^19,  3^20 is bigger than int  
    return ( n>0 &&  1162261467%n==0);
}
```