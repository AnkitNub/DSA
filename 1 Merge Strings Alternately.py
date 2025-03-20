class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1),m = len(word2)
        add_str=""
        if(n<m): #check which string is longer and add the remaining characters to the final string
            l = n #get the length of the shorter string
            add_str = word2[l:]
        elif n==m:
            l = n
        else:
            l = m
            add_str = word1[l:]
        comb_word=""
        for i in range(0,l): #merge the strings alternately getting the ith character from each string
            comb_word += word1[i] + word2[i]
        
        ans = comb_word + add_str
        return ans