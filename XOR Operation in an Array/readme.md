Given an integer n and an integer start.

* Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

* Return the bitwise XOR of all elements of nums.

 

## Example 1:

* Input: n = 5, start = 0
* Output: 8
* Explanation:   
Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.  
Where "^" corresponds to bitwise XOR operator.  
## Example 2:

* Input: n = 4, start = 3
* Output: 8
* Explanation:  
Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.  
## Example 3:

* Input: n = 1, start = 7
* Output: 7
## Example 4:

* Input: n = 10, start = 5
* Output: 2
 

## Constraints:

* 1 <= n <= 1000
* 0 <= start <= 1000
* n == nums.length

## [原題目連結點我](https://leetcode.com/problems/lexicographical-numbers/)
	
## 我的心得:
* 這題當然可以直接不斷用 ^= 得到結果，但是這樣就會是 O(n)
* 本法將所有 case 列出，所以完全不需要檢視整個數列，故時間複雜度為常數
* 實測 faster than 99.69% (用 brute force 只有 7.X %)

## 思考過程:　　
* 因為這題想了有點久，所以特此紀錄各個思考切入點:  

(1) 看題目都知道所有數字都是 +2 +2 +2 .....  
(2) 直接轉成 binary 思考，可以知道　_ _  
　　　　　　　　　　　　　　　　　　↑這格會不斷地 0,1,0,1 toggle  
(3) 故會有兩種情形：  
	一、假設一開始是長這樣 0_ ，那加二後可以得到 1_  
	　　而 1_ 的下一個又是 +2，也就是說 1_ 的下一個是 0_...  
	二、假設一開始是長這樣 1_ ，那加二後可以得到 0_  
	　　而 0_ 的下一個又是 +2，也就是說 1_ 的下一個是 1_...  
(4)上述的第一種是我想要的，為甚麼？因為 0_ 加二後**並不會進位**  
	而不會進位就代表 bit pattern 的左半部仍然為原來的樣子  
	因此我們就可以說，若 start 的 bit pattern LSB 的首兩 bit 為 0_ 形式  
	即可歸類 (start ^ (start + 2)) 為一團，此值必為 2  
(5) 所以要找 0_ 形式( _ 為 neglect 項)，就將 start % 4，看看是否小於 2  
(6) 可是萬一 start % 4 大於等於 2 呢？　　
(7) 有的可能就是 2(10)、3(11)：　　
	發現其實再 +2 又回到第 4 點所討論的情形了，意即這種情形的話就保留頭，然後作剩下 n - 1 個數列的判斷　　
(8) 接下來是判讀 n：  
	我們發現最好的 start = 0_ 時，當有 (start ^ (start + 2))，所得的值為 2  
	但卻發現 2 ^ 2 (即有四個數字)的結果為 0，然後 (0 ^ 任何數值) 的結果為該數值  
	也就是說 start = 0_ 時，總數列有 4 倍數時 XOR 的結果會為 0  
	所以要用 n % 4 判斷  
(9) 當 start = 0_ 時，若 n % 4 可以整除：  
	代表總值為 0  (即 2 ^ 2)  
	若 == 1:  
	代表最後還剩下一個，即傳回 最後一個數值 即可  
	若 == 2:  
	代表最後還剩下二個，即傳回 2  
	若 == 3:  
	代表最後還剩下三個，即傳回 (2 ^ 最後一個數值) 即可  
(10) 當 start = 1_ 時，即用第七點討論的作法即可！
	
	
