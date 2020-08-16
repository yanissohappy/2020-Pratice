Given a string s and a string t, check if s is subsequence of t.

* A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

## Follow up:
* If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

## Credits:
* Special thanks to @pbrother for adding this problem and creating all test cases.

 

## Example 1:

* Input: s = "abc", t = "ahbgdc"
* Output: true
## Example 2:

* Input: s = "axc", t = "ahbgdc"
* Output: false
 

## Constraints:

* 0 <= s.length <= 100
* 0 <= t.length <= 10^4
* Both strings consists only of lowercase characters.

## [原題目連結點我](https://leetcode.com/problems/is-subsequence/
	
## 我的心得:
* 利用 find，每次都用 s[0] 找到 t 剩下片段的第一個 index，若 index 為 -1 ，則代表找不到
* Line 23: 因為最前面剔除了 s 為空的可能，所以此處若 index_list 為空，代表甚麼東西也都找不到，此種情況是 False
* Line 23: 且若在 index_list 放進一個 -1 代表最後一次 iteration 的時候找不到對應的位置，故此種情況也是 False
* Line 26: 放進 index_list 裡的應確保是 ascending，故用 sorted 判斷是否相等