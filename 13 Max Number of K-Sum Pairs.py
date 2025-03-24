class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort() # sort the array
        n = len(nums)
        l, r, pairs = 0, n - 1, 0
        while (l<r):
            if(nums[l]+nums[r]==k): # if the sum of the two numbers is equal to k
                nums[l]=False # mark the numbers as False
                nums[r]=False
                pairs+=1  # increment the pairs
                l+=1
                r-=1
            elif nums[l]+nums[r]<k: # if the sum of the two numbers is less than k
                l+=1 # increment the left pointer
            else:
                r-=1 # decrement the right pointer
        return pairs
