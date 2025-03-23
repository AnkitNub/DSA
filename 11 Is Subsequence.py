class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t): # while the length of s is less than the length of t
            if s[i] == t[j]: # if the character in s is equal to the character in t
                i += 1 # increment i
            j += 1 # increment j
        return i == len(s) # return i is equal to the length of s