Write a function to find the longest common prefix string amongst an array of strings.

* If there is no common prefix, return an empty string "".

## Example 1:

	Input: ["flower","flow","flight"]
	Output: "fl"

## Example 2:

	Input: ["dog","racecar","car"]
	Output: ""
	Explanation: There is no common prefix among the input strings.

## Note:

* All given inputs are in lowercase letters a-z.

## [原題目連結點我](https://leetcode.com/problems/rotate-array/)

## 我的心得:
* main.py
* 在 strs 中的每個都要比對。首先先拿出 strs[0][0]，再比對 strs[1][0] 是否相等，如果不相等就直接 return，相等就繼續比較，直到比到 strs[-1][0]
* 之後要從 strs[0][1] 開始比，比到 strs[-1][1] 為止
* 如果前面的比較都順利通過，最後會比到 strs[0] 可比較的最大長度
* 此法時間複雜度為 O(單一字串長 * 總字串數)
------

* main1.py
* 同樣一開始拿 strs[0] 跟其他字串比，不一樣的話就不斷地縮減到跟該塊一樣為止，但是 strs 全部都還是要比過一次，因此時間複雜度仍為 O(單一字串長 * 總字串數)
------

* 我在網路上有看到這樣子的[解法](https://ithelp.ithome.com.tw/articles/10213258):
```python
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1        
```
* 就是直接拿出最長和最短的直接比(以短比長)，這個方法**對於這題**會是對的，原因是題目說測資只有 lowercase letters a-z
* 但是萬一 string 是有 `"12453", "24332" ...`的可能呢?
* 經實驗，`min(["14333","223","245345435"])`的結果會回傳`'14333'`，而不是`"223"`
* 所以要使回傳值為正解，要使用`min(["14333","223","245345435"], key=len)`，才會回傳`"223"`
* [原因在此](https://stackoverflow.com/questions/54023579/max-and-min-methods-in-python-returning-incorrect-values)
* 因為字串的比較都是字典順序，故`"9"`的字典順序會大於`10`，所以才要用 key 去更改判斷方式