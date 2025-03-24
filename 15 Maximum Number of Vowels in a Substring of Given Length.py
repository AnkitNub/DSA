class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        vowels="aeiou"
        initial_count=0
        for i in range(k):
            if s[i] in vowels: 
                initial_count+=1 # count the number of vowels in the first k characters
            else:
                continue
        max_count = initial_count
        for i in range(k,n):
            if s[i] in vowels and s[i-k] not in vowels: # if the current character is a vowel and the character k steps back is not a vowel
                initial_count+=1
            elif s[i] not in vowels and s[i-k] in vowels: # if the current character is not a vowel and the character k steps back is a vowel
                initial_count-=1
            max_count = max(max_count, initial_count) # update the maximum count
        return max_count
            