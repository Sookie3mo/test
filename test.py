
"""
This is the first problem I solved using Dynamic Programming and fell in 
love with DP :)
"""
"""
Problem Description:
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
#Time: O(m*n) Space: O(m+n)
#Solution:
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = [[i] for i in xrange(len(word1) + 1)]
        dis[0] = [j for j in xrange(len(word2) + 1)]
        
        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                insert = dis[i][j - 1] + 1
                delete = dis[i - 1][j] + 1
                replace = dis[i - 1][j - 1]        
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                dis[i].append(min(insert, delete, replace))
                
        return dis[-1][-1]
      
 
