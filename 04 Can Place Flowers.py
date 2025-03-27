class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0] 
        #if flower can be added at first or last point of array
        for i in range(1,len(flowerbed)-1): 
            if (flowerbed[i-1:i+2] == [0,0,0]):#check if the flower can be added at the first or last point of the array
                flowerbed[i]=1
                count+=1 #increment the count of flowers
        if count>=n:
            return True
        else:
            return False
