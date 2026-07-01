n = 2
a =[]
for i in range(n+1):
    b =list( bin(i))
    a.append(b.count('1'))
print(a)  