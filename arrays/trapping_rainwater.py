class Solution:
    def trap(self, height: list[int]) -> int:
       
     n = len(height)
     lm = [0] * n
     rm = [0] * n
     tp = 0
    
     lm[0] = height[0]
     for i in range(1, n):
         lm[i] = max(height[i], lm[i-1])
    
     rm[n-1] = height[n-1]
     for i in range(n-2, -1, -1):
         rm[i] = max(height[i], rm[i+1])
     
     for i in range(n):
         wl = min(lm[i], rm[i])
         tp += wl - height[i]
    
     return tp