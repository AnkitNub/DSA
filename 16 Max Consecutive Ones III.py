class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0: # if the current element is 0, decrement k
                k -= 1 
            if k < 0:
                if nums[left] == 0: # if the left element is 0, increment k
                    k += 1 # increment k
                left += 1 # increment left
        return right - left + 1 # return the length of the longest subarray