# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        def through(root):
            nonlocal result
            if not root:
                return 0,0
            left_sum, left_count = through(root.left)
            right_sum, right_count = through(root.right)

            current_sum = root.val+left_sum+right_sum
            current_count = left_count + right_count + 1
            if root.val == current_sum//current_count:
                result+=1
            return current_sum, current_count
        through(root)
        return result

#用nonlocal来在through里面修改result，先是basecase， 后面开始recursion， round down用//即可
