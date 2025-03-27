class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i, idx = 0, 0
        while i < len(chars):
            curr = chars[i] 
            count = 0
            while i < len(chars) and chars[i] == curr: #count the number of times the character appears
                count += 1
                i += 1
            chars[idx] = curr #store the character
            idx += 1
            if count > 1:
                for c in str(count): 
                    chars[idx] = c #store the count of the character
                    idx += 1      
        return idx