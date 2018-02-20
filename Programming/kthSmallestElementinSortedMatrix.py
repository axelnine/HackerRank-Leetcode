from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return sorted([item for sublist in matrix for item in sublist])[k-1]
        #return list(heapq.merge(*matrix))[k-1]
