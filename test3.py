numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9
# Expected output: (2, 7), (4, 5), (8, 1)
se=[]
for i in range(len(numbers)):
    for j in range(i + 1,len(numbers)):
        if numbers[i] + numbers[j]==target:
            se.append((numbers[i],numbers[j]))
print(se)
   
