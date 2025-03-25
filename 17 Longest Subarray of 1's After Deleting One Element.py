class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        curr = 0
        ans = 0
        for i in nums:
            if i == 1:
                curr += 1 # increment the count of 1s
            else:
                ans = max(ans, curr + prev) 
                prev = curr # update the previous count
                curr = 0 
        ans = max(ans, curr + prev) # update the maximum count

        return ans-1 if ans == len(nums) else ans # return the maximum count of 1s in the subarray

# Time complexity: O(n)
# Space complexity: O(1)