You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

* It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

## Example 1:

* Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
* Output: "Sao Paulo" 
* Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
## Example 2:

* Input: paths = [["B","C"],["D","B"],["C","A"]]
* Output: "A"
* Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A".   
"B" -> "C" -> "A".   
"C" -> "A".   
"A".   
Clearly the destination city is "A".  
## Example 3:

* Input: paths = [["A","Z"]]
* Output: "Z"
 

## Constraints:

* 1 <= paths.length <= 100
* paths[i].length == 2
* 1 <= cityAi.length, cityBi.length <= 10
* cityAi != cityBi
* All strings consist of lowercase and uppercase English letters and the space character.

## [原題目連結點我](https://leetcode.com/problems/destination-city/)
	
## 我的心得:
* 此題意為可串成一個城市線，也就是說首尾都只會有一點
* 所以中間連接的點是重疊的點，也就是說可以利用 set 的特性將之排除
* main.py 這段 last_set.difference(former_set) 可以寫成 last_set - former_set