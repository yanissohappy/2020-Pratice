Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


* In Pascal's triangle, each number is the sum of the two numbers directly above it.

![avatar](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

## Example:

* Input: 5
* Output:
[  
　　　　　[1],  
　　 　　[1,1],  
　　 　[1,2,1],  
　  　[1,3,3,1],  
　   [1,4,6,4,1]  
]

## [原題目連結點我](https://leetcode.com/problems/pascals-triangle/)
	
## 我的心得:
* 不斷地 iteration 即可

---------------

* 法二：利用 left shift 和 right shift，再各自相加，即可不斷得到下一排