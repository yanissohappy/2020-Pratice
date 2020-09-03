Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

* For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

## Note: 
* The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

## [原題目連結點我](https://leetcode.com/problems/daily-temperatures/)
	
## 我的心得:
* main.py
* Brute-force，會 TLE
-----

* main1.py
* 一開始要先設好全部為 0 的 list，從最後開始做，每次都找右邊最大的值，如果當下的值比右邊還大，則當下的值變成右邊最大值；否則，就是不斷地找幾天後會比當天的溫度還高
* 但很意外地這個方法在倒數第二個測資會 TLE ，於是再改進...
-----
* main2.py
* 因為 ret 右邊的部分都是做好的，所以可以不用像 main1.py 重新一個一個比對，大幅減少 iteration
* 有點像跳房子，不斷地跳到 ret 所標示的幾天後會比當天溫暖，直到該值真正的大於吾人欲求的當天的溫度
