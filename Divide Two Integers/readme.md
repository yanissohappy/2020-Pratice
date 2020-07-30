Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

## Example 1:

* Input: dividend = 10, divisor = 3
* Output: 3
* Explanation: 10/3 = truncate(3.33333..) = 3.
## Example 2:

* Input: dividend = 7, divisor = -3
* Output: -2
* Explanation: 7/-3 = truncate(-2.33333..) = -2.
## Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

## 我的心得:
* casting很重要，我在submit之前有用另一個IDE測，當時沒有用到casting但是結果都是對的
* 所以我誤以為在leetcode上也一樣不需要用casting，結果是不一樣的，這說明了為了因應各種不同的版本，還是要有萬全的應對比較好
