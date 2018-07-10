class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return Solution.climbStairs(self,n-1)+Solution.climbStairs(self,n-2)
        