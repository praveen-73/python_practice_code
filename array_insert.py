# arr= [1,3,4,5,6]

# value=2

# arr.insert(1,value)
# print(arr)


# Delete 

# arr= [1,3,4,5,6]

# arr.remove(3)
# print(arr)

# # pop ##

# arr = [10, 20, 30, 40]

# removed = arr.pop(2)

# print("Removed:", removed)
# print("Updated:", arr)

# arr = [1, 2, 2, 3, 4, 4, 5]

# arr = list(set(arr))

# print(arr)


def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)
