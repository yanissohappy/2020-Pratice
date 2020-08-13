You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

* The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

## Example 1:

* Input: J = "aA", S = "aAAbbbb"
* Output: 3
## Example 2:

* Input: J = "z", S = "ZZ"
* Output: 0
## Note:

* S and J will consist of letters and have length at most 50.
* The characters in J are distinct.

## [原題目連結點我](https://leetcode.com/problems/jewels-and-stones/)
	
## 我的心得:
* 這題我寫完之後才知道原來可以用 count 這個函式去計數
* 若要用 count，我想搭配 map 是最快的寫法，可以寫成 sum(map(J.count, S))，一行就可以解決
* 我看討論區有人是寫 sum(s in J for s in S)，我覺得很玄乎
* 結論: 我對 python 還需要更了解才行!