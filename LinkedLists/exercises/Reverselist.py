class Solution(object):
    def addTwoLists(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: Listnode
        rtype : ListNode'''

        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 =  (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            
