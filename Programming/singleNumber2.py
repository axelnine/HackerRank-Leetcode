class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sum(set(nums))*3 - sum(nums)
        return x/ 2
            
