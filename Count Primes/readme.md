Count the number of prime numbers less than a non-negative number, n.

## Example:

	Input: 10
	Output: 4
	Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

## [原題目連結點我](https://leetcode.com/problems/count-primes/)

## 我的心得:
* main.py
* Brute force，每個小於該數的都要 loop 不斷檢查是否為 prime，所以時間複雜度為 O(n ^ 2)
* 解會是對的，但會 TLE
------

* 我在網路上看到這張圖片，真的是超棒的解  
![a](./algo.gif)
* 這種方法稱為`Sieve_of_Eratosthenes` 
* 題目要求是說小於 n 有幾個 prime，故 prime 的倍數一定都不是 prime，所以先篩掉此種倍數
* 也就是說，2(不包含2), 4, 6, 8, 10, ... 都不是 prime
* 然後 3(不包含3), 6, 9, 9, 12, ... 都不是 prime
* 要特別注意的是`j = 0`那邊，因為最一開始抓到的 prime 就是 prime，一開始抓到的是 2，不能讓他被當成 not prime，所以不能讓`j = i`
* 其實寫`j = i * k`且`k = 2; k++` 也可以，總而言之就是最一開始不可以讓 prime 被當成 not prime，是 prime 的倍數才會是 not prime
