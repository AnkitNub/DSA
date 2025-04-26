class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        if head==None or head.next==None: # If the list is empty or has only one node, return None
            return None
        slow=fast=head  # Initialize slow and fast pointers to the head of the list
        while fast and fast.next: # Traverse the list with fast pointer moving twice as fast as slow
            prev=slow # Keep track of the previous node to the slow pointer
            slow=slow.next # Move slow pointer one step forward
            fast=fast.next.next     # Move fast pointer two steps forward
        # When fast pointer reaches the end, slow pointer is at the middle node
        prev.next=slow.next     # Remove the middle node by linking the previous node to the next of the slow pointer
        # Return the modified list starting from the head
        return head