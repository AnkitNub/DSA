class RecentCounter(object):

    def __init__(self):
        self.recent_calls = deque() # Using deque for O(1) complexity on both ends

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.recent_calls.append(t)     # Add the current ping time to the deque
        threshold = t-3000 # Calculate the threshold time (3000ms before t) 
        while self.recent_calls[0] < threshold:  # Remove calls that are older than 3000ms from the deque
            self.recent_calls.popleft() # O(1) complexity for removing from the left end of deque
        print(len(self.recent_calls))
        return len(self.recent_calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)