nums = [1,2,3,4,5,6,7,8,9,10]
target = 11
low,high = 0,(len(nums) - 1)
f = False
while low <= high:
         i = (low + high)//2
         if target == nums[i]:
             print(i) 
             f = True
             break
         elif target > nums[i]:
              low = i + 1
         elif target < nums[i]:
             high = i - 1     

if f == False:    
     print(-1)