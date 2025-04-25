class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate=list(senate) # Convert string to list for mutability
        n=len(senate) # Get the length of the senate string
        D,R = deque(), deque() # Initialize two deques for Dire and Radiant senators
        for i in range(n):
            if senate[i]=="R": # If the senator is Radiant, append to R deque
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dpop,rpop=D.popleft(),R.popleft() # Pop the first senator from both deques
            if dpop<rpop:  # If the Dire senator's index is less than Radiant's, Radiant wins this round
                D.append(dpop+n)    # Append the Dire senator back to the end of the deque with an index offset by n
            else:
                R.append(rpop+n)    # Append the Radiant senator back to the end of the deque with an index offset by n
        
        if not D:
            return "Radiant" 
        else:
            return "Dire"