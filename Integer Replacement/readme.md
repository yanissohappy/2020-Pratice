Given a positive integer n and you can do operations as follow:

* If n is even, replace n with n/2.
* If n is odd, you can replace n with either n + 1 or n - 1.
* What is the minimum number of replacements needed for n to become 1?

## Example 1:

* Input:
8

* Output:
3

* Explanation:
8 -> 4 -> 2 -> 1
## Example 2:

* Input:
7

* Output:
4

* Explanation:
7 -> 8 -> 4 -> 2 -> 1  
or  
7 -> 6 -> 3 -> 2 -> 1  

## [原題目連結點我](https://leetcode.com/problems/integer-replacement/)
	
## 我的心得:
* 使用 greedy
* 目標是快速 shrink 到 1
* 所以不斷地 loop，是偶數就一直不斷地 /2 (最快速到底的方式)
* 若做到奇數， +1 , -1 皆會是偶數，但有種情況是 +1 或 -1 後再除以 2 會變成奇數，這樣數字又會卡住一次(?)，很不優
* 而 奇數 > 3 的情況下， (奇數 + 1) 或 (奇數 - 1) 必為 4 的倍數，有 4 的倍數就代表可以一次除以 2 次
* 以 53 為例:
	53 + 1 = 54 -> 54 / 2 = 27 ( 2 steps) 但 27 還要思考要怎麼樣才有辦法再除以 2 (多一個 step )  
	53 - 1 = 52 -> 52 / 2 = 26 ( 2 steps) 而 26 就可以直接除以 2  
* 發現了這樣的事情就 implement 這種方法，所得的 step 即為所求   