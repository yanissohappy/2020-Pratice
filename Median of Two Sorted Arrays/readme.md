There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

## Example 1:

* nums1 = [1, 3]
* nums2 = [2]

* The median is 2.0

## Example 2:

* nums1 = [1, 2]
* nums2 = [3, 4]

* The median is (2 + 3)/2 = 2.5

## 我的心得:

* 這題要考量的東西很多，我的方法是每次都從兩條裡面找最小的，找到就把它紀錄為當前回合的最大值，並且從list拔掉
* 直到找到兩條list總數的一半就可以停止(總數是5的話就找2次，6的話就找3次)
* 再依照總數是奇數或偶數輸出答案
* 如此就可以達成O(m+n)，此法亦不用管兩條list剩下的東西，所以這個演算法應該還不錯，只是code長得不太好看X-)