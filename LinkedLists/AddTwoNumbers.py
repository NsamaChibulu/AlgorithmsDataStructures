# 1. Definition of a linked list 
# class ListNode(object):
#    def __int__(self, val=0, next=None):
#        self.val = val
#        self.next = next 

class Soltuion(object):
    def addTwoNumbers(l1, l2):
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ListNode = 1
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            p = (l1.val if l1 else 0) 
            q = (l2.val if l2 else 0)
            sum = p + q + carry
            carry, out = divmod(sum, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l1 else None)

        return result.next


    print(addTwoNumbers([2,4,3], [5,6,4]))





    


