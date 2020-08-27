Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

## Example 1:

	Input: A = "ab", B = "ba"
	Output: true

## Example 2:

	Input: A = "ab", B = "ab"
	Output: false

## Example 3:

	Input: A = "aa", B = "aa"
	Output: true

## Example 4:

	Input: A = "aaaaaaabc", B = "aaaaaaacb"
	Output: true

## Example 5:

	Input: A = "", B = "aa"
	Output: false
 

## Constraints:

	0 <= A.length <= 20000
	0 <= B.length <= 20000
	A and B consist only of lowercase letters.

## [原題目連結點我](https://leetcode.com/problems/buddy-strings/)
	
## 我的心得:
* main.py
* 想好 case 就好，不過我好像有多想以至於有些 case 會有重疊的部分
* 要注意這種情況 `aabcde aabcde` 看起來好像不能 swap，但其實可以(用 a 換)
* 所以要檢查若兩個字串相同時是否有重複項，有的話就要 return True