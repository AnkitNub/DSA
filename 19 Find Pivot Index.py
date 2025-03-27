class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums[1:]) # sum of all elements except the first one
        for i in range(len(nums)-1):
            if left == right:  # if left sum is equal to right sum,
                return i
            left += nums[i]  # add the current element to the left sum
            right -= nums[i+1]  # subtract the next element from the right sum
            if left == right:   # if left sum is equal to right sum,
                return i+1
        if len(nums) == 1:  # if there is only one element in the list,
            return 0
        return -1 