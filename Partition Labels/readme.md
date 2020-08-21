A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

## Example 1:

* Input: S = "ababcbacadefegdehijhklij"
* Output: [9,7,8]
* Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".  
This is a partition so that each letter appears in at most one part.  
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.  
 

## Note:

* S will have length in range [1, 500].
* S will consist of lowercase English letters ('a' to 'z') only.

## [原題目連結點我](https://leetcode.com/problems/partition-labels/)
	
## 我的心得:
* main.py
	1. 每次都要記錄起始點
	2. 然後從該起始點開始找最遠的( use **rfind** )
	3. if 有找到: 再來從起始點到第一次找最遠的點 iterate 中間的點們 不斷找這些中間點的下一個最遠點在哪 ( use **max** )
	4. if 沒有找到: 代表該點就是可獨立分割的
-----
* main1.py
* 微調 main.py 版本的
* 不把所有點放進一個 list 中，取而代之直接計算該 list 會有幾個個數，省去 call API 的時間(但相差不大)

-----
* main2.py
* 我看到討論區說可以利用 `{key: index for index, key in enumerate(S)}` 先找好每一個字母最右方的 index
* 這樣就不用在每次 iteration 時都還要一直找該 substring 每個字母的最右方的 index 之中的最大值(好繞口)
* 於是就實作了這個版本，比前面的效能好非常多! ( faster than 98.04% )
