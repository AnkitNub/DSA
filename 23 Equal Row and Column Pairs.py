class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hm = {}

        for ele in grid:
            ele = tuple(ele) # converting the list to a tuple to use it as a key in the dictionary
            if(ele not in hm): # if the tuple is not in the dictionary, add it with a value of 1
                hm[ele]=1
            else:
                hm[ele]+=1
        result = 0
        # print(hm)
        for i in range(len(grid[0])): # iterating through the columns of the grid
            temp = []
            for j in range(len(grid[0])): # iterating through the rows of the grid
                temp.append(grid[j][i])
            # print(temp,"temp")
            if(hm.get(tuple(temp))!=None): # if the tuple is in the dictionary, add its value to the result
                result+= hm.get(tuple(temp))
        return result