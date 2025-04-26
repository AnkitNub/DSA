# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next: # If the list is empty or has only one node, return the head
            return head
        odd, even = head, head.next
        even_head = even 
        while even and even.next:  # Traverse the list until the end of the even nodes
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next  # Link the odd node to the next odd node
            even = even.next
        odd.next = even_head    # Link the last odd node to the head of the even nodes
        return head