class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2) == (str2+str1): #check if the strings are equal if equal only then the common divisor exists
            lengthOfCommonDivisor = gcd(len(str1), len(str2))  # get the length of the common divisor
            return str1[0:lengthOfCommonDivisor] #return the common divisor
        return ""