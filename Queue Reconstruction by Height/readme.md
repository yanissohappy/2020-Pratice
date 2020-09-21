Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

## Note:
* The number of people is less than 1,100.

 
## Example

	Input:
	[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

	Output:
	[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

## [原題目連結點我](https://leetcode.com/problems/queue-reconstruction-by-height/)

## 我的心得:
* main.py
* 這次我學到了要如何根據 list[0] 和 list[1] sort 一個 list
* 這個方法我是看討論區學的，覺得太聰明了，記錄下來
* 首先要先根據 people[0] 做 descending sort，然後再根據 people[1] 做 ascending sort，不過這部分的函式我寫失敗了，中間計算的邏輯是正確的，但是在排序的時候要額外拉出來，最後再寫回去
* 也就是以下的邏輯:

```python
	a = [5, 6, 1, 0, 2]
	a_part_sorted = sort(a[1:4]) # 排序a[1], a[2], ... a[3]
	a[1:4] = a_part_sorted # 最終要寫回
```

* 總而言之這次的程式我也學到如何直接用 sort 的 key 
* 最後再開始一一排回去，排回去的方法都是根據 k 多少，因為我們已經根據身高由高到低排了，然後 k 是由小到大排，所以這樣插入回答案 list 一定保證是正確的
* 討論區的姊是如下:

```python
	[[7,0]] (insert [7,0] at index 0)
	[[7,0],[7,1]] (insert [7,1] at index 1)
	[[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
	[[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
	[[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
	[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)
```

----

* main1.py
* 我用自己的函式對 index 1 的元素 sort 成功了! 確實要額外再用一個 list 存，然後再 assign 回去