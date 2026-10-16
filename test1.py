matrix = [
    [1, 0, 0],
    [4, 5, 0],
    [7, 8, 9]
]

n = len(matrix)
result = True

for i in range(n):
    for j in range(n):
        if j > i:
            if matrix[i][j] != 0:
                result = False

if result:
    print("Lower Triangular Matrix")
else:
    print("Not a Lower Triangular Matrix")