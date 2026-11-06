# class Solution(object):
#     def removeDuplicates(self, nums):

#         num=[]
#         unique=[]
#         count=0
#         counting=0
#         for i in nums:
            
#             counting=counting+1
#             i=int(i)
#             if i not in num:
#                 num.append(i)
#                 count=count+1
#         if counting == count:
#             print(num)
#         else:
#             values = counting - count 
#             num.extend(['_'] * values)
#             print(str(num).replace("'_'","_"))
# nums=input("enter the number").split()
# obj=Solution()
# obj.removeDuplicates(nums)

                

# class Solution(object):
#     def removeDuplicates(self, nums):

#         num = []
#         count = 0

#         for i in nums:
#             if i not in num:
#                 num.append(i)
#                 count = count + 1
count=3
num=[1,2,3]
nums=[1,2,3,2,3]

for i in range(count):
    nums[i] = num[i]

print(count)

