Alice and Bob take turns playing a game, with Alice starting first.

* Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

* Choosing any x with 0 < x < N and N % x == 0.
* Replacing the number N on the chalkboard with N - x.
* Also, if a player cannot make a move, they lose the game.

* Return True if and only if Alice wins the game, assuming both players play optimally.

 

## Example 1:

	Input: 2
	Output: true
	Explanation: Alice chooses 1, and Bob has no more moves.

## Example 2:

	Input: 3
	Output: false
	Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

## Note:

* 1 <= N <= 1000

## [原題目連結點我](https://leetcode.com/problems/divisor-game/)
	
## 我的心得:
* main.py
* `return N % 2 == 0` 就可以了
* 說明：
	1. 因為正整數可以分成 even 和 odd，就結果論，只要當下取得的數字為 1 時，該人就會輸。
	2. Alice 取得先手，若 Alice 一開始得到的是偶數，則她可以做兩件事:
		(1) 將`該數 - 1`，則值會變成奇數，並且將`該數 - 1`傳給 Bob
		(2) 將`該數 ÷ 某個偶數`，則值會變成偶數，並且將`該數 ÷ 某個偶數`傳給 Bob
	3. 但我們要思考第二點的那兩條哪一個會是 optimally :
		(1) 若 Alice 走`該數 - 1`，則 Bob 能做的事只有再將`該數 - 1` 或者是 `該數 ÷ 某一個奇數`(然後結果仍為奇數)，則 Alice 必勝
		(2) 若 Alice 走`該數 ÷ 某個偶數`，這不是好事，因為傳給 Bob 的值會變成偶數，變成 Bob 如`3-(1)`小點所述取得先機，這樣就會輸
	4. 所以仔細觀察，就可以發現其實都只是奇數偶數的換來換去且值愈來愈小這樣!	