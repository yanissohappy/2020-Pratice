Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

## Example 1:

* Input: "Hello"
* Output: "hello"
## Example 2:

* Input: "here"
* Output: "here"
## Example 3:

* Input: "LOVELY"
* Output: "lovely"

## [原題目連結點我](https://leetcode.com/problems/to-lower-case/)
	
## 我的心得:
* main.py
* 刻意不使用 API
* 要注意到像是 ,.+=-()... 此類符號都不能被換成其他符號
* 所以實作時應該要從大寫的下手，一開始我是從小寫的下手，再用 else 去完成大寫的事情
* 但殊不知這種做法卻會使得 ,.+=-()... 這類符號也被囊擴在裡面了，不可不慎
-----
* main1.py
* 我在討論區看到一個可以改進效能的作法:
	因為 string is immutable，所以每次在 string 後面串東西都會產生新的 string
	因此可以用 list，最後再 return 字串回去即可
* 不過實作後只有多快了 7%

------
* 另外看到一個 **one liner** 作法，覺得很簡潔，特此紀錄:

```python

class Solution:
    def toLowerCase(self, str: str) -> str:
       return ''.join([chr(ord(char)+32) if ord(char) in range(65,91) else char for char in str ])

```