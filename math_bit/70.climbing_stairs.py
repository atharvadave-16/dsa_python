import math
n = int(input())
a = n//2
b = 0
for i in range(0,a+1):
    c = math.factorial((n - 2*i)+i)/(math.factorial(n - 2*i)*math.factorial(i))
    b = b + c

print(int(b))    
    