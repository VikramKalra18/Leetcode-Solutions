# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left, in_right):
            nonlocal post_idx
            if in_left > in_right:
                return None
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1
            idx = idx_map[root_val]
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)
            return root

        post_idx = len(postorder) - 1
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)