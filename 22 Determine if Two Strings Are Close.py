from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        dic1, dic2 = {}, {}
        for i in range(len(word1)):
            dic1[word1[i]] = dic1.get(word1[i], 0) + 1 # for each element putting them in dictionary as keys and their occurences as values
            dic2[word2[i]] = dic2.get(word2[i], 0) + 1 # for each element putting them in dictionary as keys and their occurences as values
        # Check if the keys of both dictionaries are the same and if the values are the same when counted
        if set(dic1.keys()) != set(dic2.keys()):
            return False
        return Counter(dic1.values()) == Counter(dic2.values()) # Check if the keys of both dictionaries are the same and if the values are the same when counted