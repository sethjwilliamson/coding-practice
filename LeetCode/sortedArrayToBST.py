# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid = int(len(nums) / 2)
            
            tn = TreeNode(nums[mid])
        
            tn.left = self.sortedArrayToBST(nums[:mid])
            tn.right = self.sortedArrayToBST(nums[mid+1:])
            
            return tn