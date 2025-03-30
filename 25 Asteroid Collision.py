class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i) # if the asteroid is moving to the right, add it to the stack
            else:
                while stack and stack[-1]>0: # while there are elements in the stack and the last element is positive
                    if abs(i) > stack[-1]: # if the absolute value of the current asteroid is greater than the last element in the stack
                        stack.pop() # pop the last element from the stack
                        continue # continue to check the next element in the stack
                    elif abs(i) == stack[-1]: # if the absolute value of the current asteroid is equal to the last element in the stack
                        stack.pop() # pop the last element from the stack
                    break # break the loop if the current asteroid is smaller or equal to the last element in the stack
                else:
                    stack.append(i) # if the loop ends without breaking, it means the current asteroid is moving to the left and there are no positive asteroids in the stack, so add it to the stack
        return stack
