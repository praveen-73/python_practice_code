# inpu='tommorrow'

# count=0
# values=[]
# for i in inpu:
#     if i=='o':
#         count=count+1
#         i=count* '*'
#         values.append(i)
#     else:
#         values.append(i)
# print("".join(values))

# for i in range(len(values)):
#     for j in range(1+i,len(values)):
#         if values[i]>values[j]:
#             tem=values[i]
#             values[i]=values[j]
#             values[j]=tem


# print("".join(values))
l1 = [2,4,3]
l2 = [5,6,4]
values=[]
for i in range(len(l1)):
    result=l1[i]+l2[i]
    values.append(result)
print(values)