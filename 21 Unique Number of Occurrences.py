class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for i in arr: # for each element putting them in dictionary as keys and their occurences as values
            if i in dic:
                dic[i] += 1 
            else:
                dic[i] = 1
                
        if len(set(dic.values())) != len(set(arr)): # if the number of unique values in the dictionary is not equal to the number of unique values in the list,
            return False
        return True