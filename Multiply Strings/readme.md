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
* 因為題目有禁止使用直接轉換，不然以 python 這個強大方便的語言，就可以快速寫完了
* 像是如此 return str(int(num1)*int(num2)) ←直覺想到的
* 所以就是 chr 和 ord 這兩個來一一轉換每個char的ASCII code
* 原本我以為 python 跟 C 一樣都是'1'-48就可以直接轉成1了
* 但是 C 和 python 的特性截然不同，所以要使用chr和ord幫助撰寫(也許有其他方法?待思考)

* 在這次的程式碼中還有使用到[::-1]這個東西，這是 slicing 的倒序應用
* 因為我要使用 string reverse()時發現不能這樣用（只有list可以）
* 所以用 slice 是最快的(而且list也可以使用！)
* 使用時要小心的是[::-1]前面不須放點，直接黏著便是

* (修改):我後來新增了 main2.py，這裡修改在最後的部分，原先的方法是從後面塞完 list 再 reverse ，但是我後來想會使得 iterate list 太多遍，於是直接用"insert"的方式將數值放入 list ，此放入的方式就可以直接放在最前面 e.g List.insert(0,要放入的數值)，如此就可以改善效能，最後的 submissions 上升了 19% 左右 
