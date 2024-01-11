from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int | None = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
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
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        """
        二分木のルートが与えられた場合、異なるノード a と b が存在する場合の最大値 v を見つけます (v = |a.val - b.val|)。 そして、a は b の祖先です。

        a の子が b と等しいか、a の子が b の祖先であるかのいずれかの場合、ノード a は b の祖先になります。

        - Time complexity: O(n)
        - Space complexity: O(h)

        #DFS

        Args:
            root (TreeNode | None): 二分木

        Returns:
            int: v = |a.val - b.val|
        """

        def dfs(node: TreeNode | None, min_value: int, max_value: int) -> int:
            if node is None or node.val is None:
                return max_value - min_value

            # print(f"node={node.val}, min_value={min_value}, max_value={max_value}")

            min_value = min(min_value, node.val)
            max_value = max(max_value, node.val)

            return max(
                dfs(node.left, min_value, max_value),
                dfs(node.right, min_value, max_value),
            )

        return dfs(root, 10**9 + 1, -1)


sol = Solution()
print(
    sol.maxAncestorDiff(
        root=create_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    )
)
print(sol.maxAncestorDiff(root=create_tree([1, None, 2, None, 0, 3])))
