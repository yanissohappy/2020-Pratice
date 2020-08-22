You have a list of words and a pattern, and you want to know which words in words matches the pattern.

* A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

* (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

* Return a list of the words in words that match the given pattern. 

* You may return the answer in any order.

 

## Example 1:

* Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
* Output: ["mee","aqq"]
* Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.   
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,  
since a and b map to the same letter.  
 

## Note:

* 1 <= words.length <= 50
* 1 <= pattern.length = words[i].length <= 20

## [原題目連結點我](https://leetcode.com/problems/find-and-replace-pattern/)
	
## 我的心得:
* main.py
* 這題 __bijection__ 其實就是 [Isomorphic Strings](https://github.com/yanissohappy/Pratice/tree/master/Isomorphic%20Strings) 的問題
* 但這次用不一樣的寫法(使用 dictionary + set，然後卡很久，雖然還是寫出來，但是效能不好)　
* 就是要做兩個 dictionary，然後兩者的每每 value 只能有 "eeee" 這樣的情形，而不能有 "eee**k**" 的情形
* 所以 `def checkDict(self, _dict)` 的目的就是要挑出上面的情形
-----
* main1.py
* 用較簡潔的方法完成
* 思考:
	1. 用 zip 可以抓出 ('a','b'), ('a','n'),('b','c')...
	2. ('a','b'), ('a','n')這種情形是不可以的，但無法透過知道長度而確知會不會錯誤
	3. 所以要搭配檢查 每個 word 及 pattern 的 set 長度是否跟上面那個 zip set 後的長度結果一樣

-----
* 在討論區看到的不錯的解法，利用 dict 的 setdefault

```python
    def findAndReplacePattern(self, words, p):
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        return [w for w in words if F(w) == F(p)]
```