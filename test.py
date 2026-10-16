import math

text = input("Enter a string: ")

length = len(text)
columns = math.ceil(math.sqrt(length))
rows = math.ceil(length / columns)

index = 0

for i in range(rows):
    for j in range(columns):
        if index < length:
            print(text[index], end=" ")
            index = index + 1
        else:
            print("-", end=" ")
    print()