nums = list(input())
target = int(input)
for i in range (0,len(nums)-1): 
    for j in range (i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])