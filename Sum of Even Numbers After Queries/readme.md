We have an array A of integers, and an array queries of queries.

* For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

* (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

* Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

 

## Example 1:

	Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
	Output: [8,6,2,4]
	Explanation: 
	At the beginning, the array is [1,2,3,4].
	After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
	After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
	After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
	After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
 

## Note:

* 1 <= A.length <= 10000
* -10000 <= A[i] <= 10000
* 1 <= queries.length <= 10000
* -10000 <= queries[i][0] <= 10000
* 0 <= queries[i][1] < A.length

## [原題目連結點我](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)
	
## 我的心得:
* main.py
* 這裡一開始只使用了一次 sum ，之後再決定所加和來的數是奇數還是偶數
	1. 原來的數是偶數，加了奇數後會變成奇數，所以要從總和裡扣掉該偶數
	2. 原來的數是偶數，加了偶數後會變成偶數，所以要從總和裡加上多加上的偶數
	3. 原來的數是奇數，加了奇數後會變成偶數，所以要從總和裡加上原來的奇數及所加上得奇數
	4. 原來的數是奇數，加了偶數後會變成奇數，是完全不用管的 case
----
* badsol.py
* 這是結果也正確，但是會 TLE 的寫法，原因是每次還要用整個 list 重新尋找偶數和，這樣在[超大測資](./bigdata.txt)的時候會出錯
