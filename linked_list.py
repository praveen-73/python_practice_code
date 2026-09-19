# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# s1=Node(10)
# s2=Node(20)
# s3=Node(30)

# s1.next=s2
# s2.next=s3

# current=s1
# while current is not None:
#     print(current.data)
#     current=current.next
############################################################################################
# double linked list    


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Link nodes
n1.next = n2
n2.prev = n1

n2.next = n3
n3.prev = n2

# Forward traversal
print("Forward:")
temp = n1
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next

print("None")


# Backward traversal
print("Backward:")
temp = n3
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.prev

print("None")
######################################################################################
#circular linked list  



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Link nodes
n1.next = n2
n2.next = n3
n3.next = n1   # circular connection

# Traverse circular linked list
temp = n1
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == n1:   # stop when back to head
        break

print("(back to head)")