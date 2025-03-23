class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i=0
        for j in range(n):
            if nums[j]!=0: # if the number is not zero
                nums[i] , nums[j] = nums[j] , nums[i]  # swap the number with the first zero
                i+=1