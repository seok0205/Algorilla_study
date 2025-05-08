arr = [[1,2,3] for _ in range(3)]
print(list(map(list, zip(*arr))))
print([row[::-1] for row in arr])
print(list(map(list, zip(*arr)))[::-1])
print(list(map(list, zip(*arr[::-1]))))
[(1, 1, 1),
 (2, 2, 2), 
 (3, 3, 3)]
[1 , 2, 3]
[1 , 2, 3]
[1 , 2, 3]

[[3, 2, 1],
 [3, 2, 1],
 [3, 2, 1]]

[[3, 3, 3],
 [2, 2, 2],
 [1, 1, 1]]
