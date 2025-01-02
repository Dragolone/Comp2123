class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def list_to_number(node):
            num = 0
            multiplier = 1
            while node:
                num += node.val * multiplier
                multiplier *= 10
                node = node.next
            return num

        def number_to_list(num):
            dummy = ListNode(0)
            current = dummy
            if num == 0:
                return ListNode(0)
            while num > 0:
                current.next = ListNode(num % 10)
                num //= 10
                current = current.next
            return dummy.next

        num1 = list_to_number(l1)
        num2 = list_to_number(l2)
        num3 = num1 + num2

        return number_to_list(num3)