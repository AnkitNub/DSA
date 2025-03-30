class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i == '*': # pop the last character from the stack if we encounter a star
                stack.pop()
            else:
                stack.append(i) # otherwise, add the character to the stack
        return "".join(stack) # join the characters in the stack to form the final string
            
