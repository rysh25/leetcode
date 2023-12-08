from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int | None = 0,
        left: "TreeNode" | None = None,
        right: "TreeNode" | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def create_tree(list: list[int | None]):
    from collections import deque

    if not list:
        return

    root = TreeNode(list[0])
    parent = root
    q: deque[TreeNode] = deque()
    q.append(root)
    i = 1
    while len(q):
        parent = q.popleft()
        if i < len(list) and list[i] is not None:
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.append(node)
            parent.left = node
        i += 1
        if i < len(list) and list[i] is not None:
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.append(node)
            parent.right = node
        i += 1

    return root


class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        def dfs(v: TreeNode) -> str:
            ret = str(v.val)
            if v.left is None and v.right is None:
                return str(v.val)
            ret += "("
            if v.left is not None:
                ret += dfs(v.left)
            ret += ")"
            if v.right is not None:
                ret += "(" + dfs(v.right) + ")"
            return ret

        return dfs(root) if root is not None else ""


sol = Solution()
root = create_tree([1, 2, 3, 4])
print(sol.tree2str(root=root))
root = create_tree([1, 2, 3, None, 4])
print(sol.tree2str(root=root))
