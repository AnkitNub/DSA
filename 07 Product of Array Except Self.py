class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n #initialize the list with 1s
        
        left_mult = 1
        for i in range(n):
            ans[i] = left_mult #store the product of the left side of the element
            left_mult *= nums[i] #update the left_mult

        right_mult = 1
        for i in range(n - 1, -1, -1): #iterate from the end of the list
            ans[i] *= right_mult #multiply the product of the left side of the element with the product of the right side of the element
            right_mult *= nums[i] #update the right_mult

        return ans