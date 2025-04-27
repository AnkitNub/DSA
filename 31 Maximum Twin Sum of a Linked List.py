# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        nums = []
        curr = head
        while curr:       # Traverse the linked list and store the values in a list
            nums.append(curr.val)       
            curr = curr.next        
        
        N = len(nums)
        res = 0
        for i in range(N // 2):
            res = max(res, nums[i] + nums[N - i - 1])   # Calculate the maximum twin sum
        return res