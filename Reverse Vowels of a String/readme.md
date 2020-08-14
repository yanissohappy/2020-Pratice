Write a function that takes a string as input and reverse only the vowels of a string.

## Example 1:

* Input: "hello"
* Output: "holle"
## Example 2:

* Input: "leetcode"
* Output: "leotcede"
## Note:
* The vowels does not include the letter "y".

## [原題目連結點我](https://leetcode.com/problems/reverse-vowels-of-a-string/)
	
## 我的心得:
* main.py
* 在該塞東西的地方塞好就好！:D　只是這個效能有點慘(汗)
----

* main1.py
* 在得到母音字元同時也紀錄該位置，最後在該位置用先存好的母音 list pop 出來覆蓋掉( pop default 從最後一個)，但此種方法須搭配 list 使用
* 利用空間換時間，這樣效能就大幅躍進了
