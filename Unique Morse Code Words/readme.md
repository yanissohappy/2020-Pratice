International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

* For convenience, the full table for the 26 letters of the English alphabet is given below:

    	[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

* Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

* Return the number of different transformations among all words we have.

## Example:
* Input: words = ["gin", "zen", "gig", "msg"]
* Output: 2
* Explanation:  
The transformation of each word is:  
"gin" -> "--...-."  
"zen" -> "--...-."  
"gig" -> "--...--."  
"msg" -> "--...--."  

*There are 2 different transformations, "--...-." and "--...--.".
## Note:

* The length of words will be at most 100.
* Each words[i] will have length in range [1, 12].
* words[i] will only consist of lowercase letters.

## [原題目連結點我](https://leetcode.com/problems/unique-morse-code-words/)
	
## 我的心得:
* 利用 ord 去取得 ASCII，以便計算在 alphabet 對應的位置
* 再利用 set 不重複特性來計算 distinct 個體數即可
------
* 在討論區我看到有人使用 zip 以及 string.ascii_lowercase (即列出 'abcdefghijklmnopqrstuvwxyz' )，覺得很巧妙，特此紀錄

		morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		import string
		morsedict = dict(zip(string.ascii_lowercase,morse))
* 然後再利用 key value 輸出即可
