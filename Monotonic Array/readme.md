An array is monotonic if it is either monotone increasing or monotone decreasing.

* An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

* Return true if and only if the given array A is monotonic.

 

## Example 1:

	Input: [1,2,2,3]
	Output: true

## Example 2:

	Input: [6,5,4,4]
	Output: true

## Example 3:

	Input: [1,3,2]
	Output: false

## Example 4:

	Input: [1,2,4,5]
	Output: true

## Example 5:

	Input: [1,1,1]
	Output: true
 

## Note:

* 1 <= A.length <= 50000
* -100000 <= A[i] <= 100000

## [原題目連結點我](https://leetcode.com/problems/monotonic-array/)
	
## 我的心得:
* main.py
* 要注意的是這種 case `[1,1,0]`
* 一開始我的寫法是:
```python
            """
            if A[1] >= A[0]:
                return sorted(A) == A
            else:
                return sorted(A, reverse = True) == A
            """
```
* 覺得只要測試前兩個就可以了，殊不知會有這種相等的測資，可以檢測出我的思考盲區
* 所以後來我就改成
```python
            ascending = sorted(A)
            descending = sorted(A, reverse = True) 
            return ascending == A or descending == A
```
* 這樣的寫法只要 ascend sort 或 descend sort 其一為對就對(因為有排序的結果只會有這兩種情形)