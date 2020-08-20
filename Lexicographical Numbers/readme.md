Given an integer n, return 1 - n in lexicographical order.

* For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

* Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

## [原題目連結點我](https://leetcode.com/problems/lexicographical-numbers/)
	
## 我的心得:
* main.py (faster than 34.29%)
* 確定是可以的做法，但是值超過 700000 會 TLE，但其實 commit 的話是可以 pass的

-----
* main1.py (faster than 6X%)
* 改進的作法，同樣也是 BFS 的概念，而且因為不用不斷用 queue 存，所以速度快了一些