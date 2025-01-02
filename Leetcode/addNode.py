def addTwoNumbers(l1:list, l2:list):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    length1 = len(l1)
    length11 = length1
    length2 = len(l2)
    length22 = length2
    num1 = 0
    num2 = 0
    for i in range(length1 - 1, -1, -1):
        num1 += 10 ** (length11 - 1) * l1[length11 - 1]
        # print(num1)
        length11 -= 1
    for j in range(length2 - 1, -1, -1):
        num2 += 10 ** (length22 - 1) * l2[length22 - 1]
        length22 -= 1
    num3 = num1 + num2
    print(num3)
    l3 = []
    length3 = len(str(num3))
    while num3 > 0:
        l3.append(num3 % 10)
        num3 //= 10
    return l3

print(addTwoNumbers([1, 2, 3, 6, 9], [2, 4, 5]))

