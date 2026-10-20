# matrix = [
#     [1, 0, 0],
#     [4, 5, 0],
#     [7, 8, 9]
# ]

# n = len(matrix)
# result = True

# for i in range(n):
#     for j in range(n):
#         if j > i:
#             if matrix[i][j] != 0:
#                 result = False

# if result:
#     print("Lower Triangular Matrix")
# else:
#     print("Not a Lower Triangular Matrix")


def multiple(a,b):
    total=0
    for i in range(b):
        total=total+a
    return total

def facatorial(n):
    result=1
    for i in range(1,n+1):
        result=multiple(result,i)
    return result

n=int(input("enter the number"))
print(facatorial(n))