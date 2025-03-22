class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for num in nums:
            if num<=first: #if the number is less than or equal to the first number
                first=num
            elif num<=second: #if the number is less than or equal to the second number
                second=num
            else:
                return True #if the number is greater than the first and second number
        return False