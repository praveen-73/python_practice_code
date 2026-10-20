# def alpha(char):
#     character=list(char)

#     for i in range(len(character)):
#         for j in range(i+1, len(character)):
#             if character[i]>character[j]:
#                 tem=character[i]
#                 character[i]=character[j]
#                 character[j]=tem
#     print("".join (character))
# val=input("ENTER THE VALUE")
# alpha(val)


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())