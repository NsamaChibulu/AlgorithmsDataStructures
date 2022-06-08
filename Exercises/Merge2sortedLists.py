class solution:
    def mergeTwoLists(self, list1, list2):
        # maintain an unchnaging reference to the node ahead of the return node
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
            else:
                prev.next = list2
                list2 = list2.next
            prev.next = list2

            # At least one of list1 and list2 can still have nodes at this point, so 
            # connect the non-null list to the end of the merged list.

        prev.next = list1 if list1 is not None else list2

        return prehead.next 
            