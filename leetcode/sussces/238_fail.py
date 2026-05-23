from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        temp = 1
        
        for left in range(n):
            result[left] = temp      
            temp *= nums[left]       
            
        temp = 1
        
        for right in range(n - 1, -1, -1):
            result[right] *= temp    
            temp *= nums[right]      
            
        return result