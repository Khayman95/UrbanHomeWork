n = input('Введите n (от 3х до 20ти): ')
result = []
m = 1
o = []
p = []
k = int(n)
for j in range(1,k):
    for i in range(1,k):
        if k % (i + j) == 0 and i != j and i >= j:
            o.append(i)
            p.append(j)
        i = i+1
    j = j+1
for j,i in zip(p,o):
    result += [j,i]
print(result)