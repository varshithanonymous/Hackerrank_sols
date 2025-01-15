# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Dummy node to simplify merging logic
        current = dummy  # Pointer to build the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Link to list1's node
                list1 = list1.next  # Move to the next node in list1
            else:
                current.next = list2  # Link to list2's node
                list2 = list2.next  # Move to the next node in list2
            current = current.next  # Move current pointer

        # Attach remaining nodes if one list is exhausted
        current.next = list1 if list1 else list2

        return dummy.next  # Return the head of the merged list