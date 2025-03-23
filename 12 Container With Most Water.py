class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n-1
        area = []
        while (l!=r):
            if(height[l]<height[r]): # if the height of the left pointer is less than the height of the right pointer
                area.append(height[l]*(r-l)) # append the area to the list
                l+=1
            else:
                area.append(height[r]*(r-l)) 
                r-=1
        highest = 0
        for i in range(len(area)): # loop to find the max area we recoverd so far
            if(area[i]>highest):
                highest=area[i]
        return highest 