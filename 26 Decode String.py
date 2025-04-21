class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for i in range(len(s)): # iterate through the string
            
            if s[i] != ']':
                stack.append(s[i]) # if the character is not a closing bracket, add it to the stack
                
            else:
                subStr = ''
                while stack[-1] != '[':  # if the character is a closing bracket, pop from the stack until we find the opening bracket
                    subStr = stack.pop() + subStr
                stack.pop()
                
                digit = ''
                while stack and stack[-1].isdigit(): # if the character is a digit, pop from the stack until we find a non-digit character
                    digit = stack.pop() + digit # build the digit string in reverse order
                    
                stack.append(int(digit) * subStr)
                
        return ''.join(stack)