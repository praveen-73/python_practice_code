class Solution(object):
    def addTwoNumbers(self, l1, l2):

        values = []
        carry = 0

        for i in range(len(l1)):
            total = l1[i] + l2[i] + carry

            values.append(total % 10)
            carry = total // 10

        if carry:
            values.append(carry)

        return values


l1 = [2, 4, 3]
l2 = [5, 6, 4]

obj = Solution()
print(obj.addTwoNumbers(l1, l2))