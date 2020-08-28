A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

* A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

* Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

* Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

## Example 1:

	Input: "(()())(())"
	Output: "()()()"
	Explanation: 
	The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
	After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

## Example 2:

	Input: "(()())(())(()(()))"
	Output: "()()()()(())"
	Explanation: 
	The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
	After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

## Example 3:

	Input: "()()"
	Output: ""
	Explanation: 
	The input string is "()()", with primitive decomposition "()" + "()".
	After removing outer parentheses of each part, this is "" + "" = "".
 

## Note:

	S.length <= 10000
	S[i] is "(" or ")"
	S is a valid parentheses string

## [原題目連結點我](https://leetcode.com/problems/remove-outermost-parentheses/)
	
## 我的心得:
* main.py
* 有記錄我寫到一半寫錯的 code
* 還是計數有幾個左括號和右括號，然後左括號和右括號個數相等時，stack 去頭去尾後一次放進去 return list，就萬無一失了