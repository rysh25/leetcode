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
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        """
        2 つのバイナリ ツリーは、葉の値のシーケンスが同じである場合、葉が類似しているとみなされます。

        ノード root1 と root2 を持つ 2 つの指定されたツリーが葉が類似している場合にの true を返します。

        - Time complexity: O(n1 + n2)
        - Space complexity: O(h1 + h2) * h1 and h2 are the heights of the two trees.

        #DFS

        Args:
            root1 (TreeNode | None): バイナリ ツリー1
            root2 (TreeNode | None): バイナリ ツリー2

        Returns:
            bool: 葉が類似している場合にの true を返します。
        """
        leaf_seq1: list[int] = []
        leaf_seq2: list[int] = []

        def dfs(node: TreeNode | None, leaf_seq: list[int]):
            if node is None or node.val is None:
                return

            if node.left is None and node.right is None:
                leaf_seq.append(node.val)
                return

            dfs(node.left, leaf_seq)
            dfs(node.right, leaf_seq)

        dfs(root1, leaf_seq1)
        dfs(root2, leaf_seq2)

        return leaf_seq1 == leaf_seq2


sol = Solution()
print(
    sol.leafSimilar(
        root1=create_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
        root2=create_tree(
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
        ),
    ),
)
print(sol.leafSimilar(root1=create_tree([1, 2, 3]), root2=create_tree([1, 3, 2])))
