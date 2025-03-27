class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        i = 0
        j = len(s)-1
        str_list = list(s)
        while i<j:
            if str_list[i] not in vowels:
                i+=1
            elif str_list[j] not in vowels:
                j-=1
            else:
                str_list[i],str_list[j] = str_list[j],str_list[i]
                i+=1
                j-=1
        return "".join(str_list)