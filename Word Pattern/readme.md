Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

## Example 1:

	Input: pattern = "abba", s = "dog cat cat dog"
	Output: true
	
## Example 2:

	Input: pattern = "abba", s = "dog cat cat fish"
	Output: false

## Example 3:

	Input: pattern = "aaaa", s = "dog cat cat dog"
	Output: false

## Example 4:

	Input: pattern = "abba", s = "dog dog dog dog"
	Output: false
 

## Constraints:

	1 <= pattern.length <= 300
	pattern contains only lower-case English letters.
	1 <= s.length <= 3000
	s contains only lower-case English letters and spaces ' '.
	s does not contain any leading or trailing spaces.
	All the words in s are separated by a single space.

## [原題目連結點我](https://leetcode.com/problems/word-pattern/)

## 我的心得:
* main.py
* 就是之前做過的 **bijection** 題目，直接使用 set 去算出各種組合的長度有沒有相等即可

-----
* main1.py
* 利用題目說 pattern 只有小寫的特性，所以使用 ASCII 在一個有 26 個 elements 的 list`str_map`紀錄
* 每次都要檢查現在那些 dog, cat 的值 有沒有出現在除了當下在做的 list 標號的其他 elements 中，若有，就是 False；若沒有，則開始檢查下面的事項
* 如果當下在做的 list 標號還沒有存入任何東西，那就放進去
* 若有存東西的話，要比對那個東西和現在相對應的 string 是否相同，不同則是 False；若沒有，則開始檢查下面的事項
* 最後全部檢查無誤後，才可以說是 True