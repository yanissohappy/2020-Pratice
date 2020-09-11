In an infinite binary tree where every node has two children, the nodes are labelled in row order.

* In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

![a](https://assets.leetcode.com/uploads/2019/06/24/tree.png)

* Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

## Example 1:

	Input: label = 14
	Output: [1,3,4,14]

## Example 2:

	Input: label = 26
	Output: [1,2,6,10,26]
 

## Constraints:

	1 <= label <= 10^6

## [原題目連結點我](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)

## 我的心得:
* main.py
* 我的方法:
	1. 先將值都放好進 tree 這個 list 裡
	2. 然後再用 label 的值，用其 index 不斷求其父節點 index，直到求到 root 為止
	3. 求父節點 index 的計算方式為:

		floor((現在 index - 1) / 2) 
* 但是效能不好，因為這是 brute force
-----

* 於是我看了討論區一個很聰明的方法，是利用 bit pattern 的思維做的，方法就是要求其 parent node 就保留 MSB 其餘 bit toggle，然後再 shift right 一位，不斷做直到 1 為止  
* [點我](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323848/Golang-O(log-n)-with-detail-explanation)  

* We first consider the normal case.

* Obviously for a specific number, we can easily find the path from root to the node labeled with the number.

* For example, 111 -> 11 -> 1, 101 -> 10 -> 1, 110 -> 11 -> 1. Just shift the number one bit to the right and we can get the parent node of the number until we meet the root node labeled with 1.
![d](https://assets.leetcode.com/users/kerojin/image_1561907141.png)

* Now we consider the zigzag case.
![b](https://assets.leetcode.com/users/kerojin/image_1561907407.png)
* Compared to the normal case, it needs to convert the node to the symmetric node on the same level and get the parent node

* For example, 100 (--symmetric-> 111) -> 11 (--symmetric-> 10) -> 1, 101 (--symmetric-> 110) -> 11 (--symmetric->10) -> 1

* How to get the symmetric of the number on the same level? The highest bit remains unchanged, the other bits are reversed

* 1110 -> 1001, we can find 1110+1001=10111=10000+1000-1, so 1001 = 10000+1000-1-1110. That is what 1<<tb + 1<<(tb-1) - 1 - n means.

		14(1110) --> 9(1001) -> 4(100)
		4(100) --> 7(111) -> 3(11)
		3(11) --> 2(10) -> 1

* so the path is 1->3->4->14

		26(11010) --> 21(10101) -> 10(1010)
		10(1010) --> 13(1101) -> 6(110)
		6(110) --> 5(101) -> 2(10)
		2(10) --> 3(11) -> 1

* so the path is 1->2->6->10->26


```golang
func pathInZigZagTree(label int) []int {
	ans := []int{label}
	for label > 1 {
		label = convert(label)
		ans = append(ans, label)
	}
	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}
	return ans
}

func convert(n int) int {
	tb := uint(bits(n))
	return symmetric(n, tb) >> 1
}

func symmetric(n int, tb uint) int {
	return 1<<tb + 1<<(tb-1) - 1 - n
}

func bits(n int) int {
	r := 0
	for n > 0 {
		r++
		n >>= 1
	}
	return r
}
```
