class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        avg = 0.0
        initial = 0.0
        for i in range(k):
            initial += nums[i] # sum of the first k elements

        avg = initial / k
        for i in range(k, n): # iterate through the array
            initial += nums[i] - nums[i - k]   # sum of the next k elements
            current_avg = initial / k # calculate the average
            if avg < current_avg:
                avg = current_avg # update the average

        return round(avg, 5) # return the average rounded to 5 decimal places