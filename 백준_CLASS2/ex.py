a = [1,2,3,4]
for i in range(1 << 4):
    temp = []
    for j in range(4):
        if i & (1 << j):
            temp.append(a[j])
    print(temp)
