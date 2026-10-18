# input1=[34,6,8,97,8]
# max_number=input1[0]
# mini_number=input1[0]
# for i in input1:
#     if i> max_number:
#         mini_number=max_number
#         max_number=i
#         #max_number.append(i)
#     elif i>mini_number and max_number!=mini_number:
#         mini_number=i
#         #mini_number.append(i)
# addition=max_number*mini_number
# print(max_number)
# print(mini_number)     
# print(addition)

values=[1,2,4,5,7,9,6,4,3,6,2,5]
for i in values:
    count=0
    for j in values:
        if i==j:
            count=count+1
    print(f"{i}count:{count}")
