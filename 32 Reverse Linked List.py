# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = None # Initialize a new list to None
        curr = head 
        while curr:  
            next_node = curr.next # Store the next node
            curr.next = new_list # Reverse the current node's pointer to point to the new list
            # Move the new list pointer to the current node
            new_list = curr
            curr = next_node
        return new_list