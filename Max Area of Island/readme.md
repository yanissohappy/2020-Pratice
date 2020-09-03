Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

* Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

## Example 1:

	[[0,0,1,0,0,0,0,1,0,0,0,0,0],
	 [0,0,0,0,0,0,0,1,1,1,0,0,0],
	 [0,1,1,0,1,0,0,0,0,0,0,0,0],
	 [0,1,0,0,1,1,0,0,1,0,1,0,0],
	 [0,1,0,0,1,1,0,0,1,1,1,0,0],
	 [0,0,0,0,0,0,0,0,0,0,1,0,0],
	 [0,0,0,0,0,0,0,1,1,1,0,0,0],
	 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
	Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

## Example 2:

	[[0,0,0,0,0,0,0,0]]
	Given the above grid, return 0.
	
## Note: 
* The length of each dimension in the given grid does not exceed 50.

## [原題目連結點我](https://leetcode.com/problems/max-area-of-island/)
	
## 我的心得:
* main.py
* 如果走到的某一點是 0，就不用遞迴；若是 1，要遞迴，每次遞迴都要把原 grid 的該點值改為 0，因為要減少重複計算量(所有連的部分只要算一次就夠了，且目的只是算最大值而已)