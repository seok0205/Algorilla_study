A = int(input())
B = int(input())
C = int(input())

mul = str(A*B*C)
cnt_lst = []
for i in range(10):
    cnt_lst.append(mul.count(str(i)))

for k in range(10):
    print(cnt_lst[k], end='\n')
