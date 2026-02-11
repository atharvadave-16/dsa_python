a =[1,2,3,4]
a = int("".join(map(str, a)))
b = a + 1
print(list(map(int, str(b))))
