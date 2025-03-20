class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        arr = []
        max_candies=0
        for i in range(n): #get the maximum number of candies
            if(candies[i]>max_candies):
                max_candies=candies[i]

        for i in range(n):
            if(candies[i]+extraCandies>=max_candies): #check if the number of candies can be the greatest
                arr.append(True)
            else:
                arr.append(False)
        return arr