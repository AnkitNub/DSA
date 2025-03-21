class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        word = ""
        str_list = []
        for i in range(n):
            if s[i] == ' ' or i == n - 1: #if the character is a space or the last character
                if i == n - 1 and s[i] != ' ': #if the last character is not a space
                    word += s[i]
                if word:
                    str_list.append(word) #append the word to the list
                word = ""
            else:
                word += s[i]

        if not str_list: #if the list is empty
            return ""
        new_s = " ".join(str_list[::-1]) #reverse the list and join the words with a space
        return new_s
