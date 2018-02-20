from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return(nums[len(nums)-k])
        
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heappush(heap,num)
        
        return nlargest(k,heap)[k-1]
        
