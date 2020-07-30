Given an array of strings, group anagrams together.

## Example:

* Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
* Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
## Note:

* All inputs will be in lowercase.
* The order of your output does not matter.

## 我的心得:
* 寫這題時的我的順序一直想錯(汗)
* 我的作法是使用dictionary比對，只要dictionary相同就相同，並要加入同一個list的list
* 每次都是用list[0]比對其他的，比對前要先拔掉list[0]，然後再比對剩下的
* 在判斷dictionary相同與否時，若相同，就可以拔掉，但要小心該index要保留為原來的(所以要用continue跳過)，因為[1,3,4,5]拔掉3後list會成為[1,4,5]，原來拔掉的3 index是1，後來的list的index為1的部分剛好是4
* 如此做法並不是最好的，因為如果遇到["abc","cdv","dwr",....](沒有一個是其中的permutation)，此即為 worst case
* 所以時間複雜度為O(n^2)
