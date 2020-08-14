There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

* You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

 

## Example 1:

* Input: groupSizes = [3,3,3,3,3,1,3]
* Output: [[5],[0,1,2],[3,4,6]]
* Explanation: 
* Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
## Example 2:

* Input: groupSizes = [2,1,3,3,3,2]
* Output: [[1],[0,5],[2,3,4]]
 

## Constraints:

* groupSizes.length == n
* 1 <= n <= 500
* 1 <= groupSizes[i] <= n

## [原題目連結點我](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/)
	
## 我的心得:
* main.py
* 是 Brute force 法

----
* main1.py 
* 效能還不錯，同樣也用到 dictionary，但是是相同次數( key )的一次放進去同個 value 裡
* 所以長相會是這樣 3:[1,2,5,7,9,...] 之類的
* 到時候要取用的時候就依其 key 決定要一次從 value 中選幾個 element 作為同一個 group
