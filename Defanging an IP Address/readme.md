Given a valid (IPv4) IP address, return a defanged version of that IP address.

* A defanged IP address replaces every period "." with "[.]".

 

## Example 1:

	Input: address = "1.1.1.1"
	Output: "1[.]1[.]1[.]1"

## Example 2:

	Input: address = "255.100.50.0"
	Output: "255[.]100[.]50[.]0"
 

## Constraints:

* The given address is a valid IPv4 address.

## [原題目連結點我](https://leetcode.com/problems/defanging-an-ip-address/)
	
## 我的心得:
* main.py
* 一格一格做就好
----
* 或是也可以如下寫:

```python
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")
```