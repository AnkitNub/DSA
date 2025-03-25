class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n = len(gain)
        ans = [0]*(n+1) #initialize the altitude array
        alt = 0
        for i in range(n):
            ans[i+1]=ans[i]+gain[i] #get the altitude at each point
            if(ans[i+1]>=alt): #get the maximum altitude
                alt = ans[i+1]
        return alt 

# Time complexity: O(n)
# Space complexity: O(n)