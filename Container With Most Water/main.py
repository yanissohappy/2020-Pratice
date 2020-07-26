def maxArea(self, height):
    """ 註解的這邊是可以的，只是會變成O(n^2)，效能很差
    max_val = 0
    val = 0
    
    total_len = len(height) - 1
    # 先從最大的寬度開始找
    
    while True: # 做到total_len為止
        if total_len == 0:
            break 
        From = 0               
        while From + total_len < len(height):
            To = From + total_len 
            if height[From] >= height[To]:
                val = height[To] * total_len
            else:
                val = height[From] * total_len
            if val >= max_val:
                max_val = val
            From += 1
        total_len -= 1
        
    return max_val
    """            

    max_val, left, right = 0, 0, len(height) - 1
    
    while left < right:
        max_val = max(max_val, min(height[right], height[left]) * (right - left))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_val
