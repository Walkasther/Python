a = ([1,2,3],[3,2,1],[4,5,6])
b = list(a)

b[1] = 7

a[2].append(9)
a[1].pop()
print(a)
print(b)