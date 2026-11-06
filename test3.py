numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
all_numbers=[]
for i in range(1,11):
    if i in numbers:
        all_numbers.append(i)
    elif i not in numbers:
            all_numbers.append(i)

print(all_numbers)
    