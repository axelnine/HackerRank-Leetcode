# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        n = max(nums)
        index=nums.index(n)
        
        node=TreeNode(n)
        
        node.left=self.constructMaximumBinaryTree(nums[0:index])
        node.right=self.constructMaximumBinaryTree(nums[index+1:])

        return node
