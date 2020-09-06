Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

* Notice that the row index starts from 0.

![f](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)  
In Pascal's triangle, each number is the sum of the two numbers directly above it.  

## Follow up:

* Could you optimize your algorithm to use only O(k) extra space?

 

## Example 1:

	Input: rowIndex = 3
	Output: [1,3,3,1]

## Example 2:

	Input: rowIndex = 0
	Output: [1]
	
## Example 3:

	Input: rowIndex = 1
	Output: [1,1]
 

## Constraints:

* 0 <= rowIndex <= 40

## [原題目連結點我](https://leetcode.com/problems/pascals-triangle-ii/)
	
## 我的心得:
* main.py
* 本題剛好用O(k) space!
* 方法就是利用數學的公式，找出 row 數與該層個數的關係，並且利用反轉 list 以達成 O(k) 的 space
* 如果該階層的個數是偶數，那就只要做一半就好，然後另一半用反轉的
* 如果該階層的個數是奇數，那就只要做到含正中間前的一半就好，然後另一半用反轉的即可
* 效能不錯， faster than 98.85% of Python online submissions
