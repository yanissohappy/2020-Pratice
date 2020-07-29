Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

## Example 1:

* Input: num1 = "2", num2 = "3"
* Output: "6"
## Example 2:

* Input: num1 = "123", num2 = "456"
* Output: "56088"
## Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

## 我的心得:
* 因為題目有禁止使用直接轉換，不然以python這個強大方便的語言，就可以快速寫完了
* 像是如此return str(int(num1)*int(num2))←直覺想到的
* 所以就是chr和ord這兩個來一一轉換每個char的ASCII code
* 原本我以為python跟C一樣都是'1'-48就可以直接轉成1了
* 但是C和python的特性截然不同，所以要使用chr和ord幫助撰寫(也許有其他方法?待思考)

* 在這次的程式碼中還有使用到[::-1]這個東西，這是slicing的倒序應用
* 因為我要使用string reverse()時發現不能這樣用（只有list可以）
* 所以用slice是最快的(而且list也可以使用！)
* 使用時要小心的是[::-1]前面不須放點，直接黏著便是
