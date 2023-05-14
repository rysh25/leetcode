from __future__ import annotations

from collections import deque


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


def print_tree(name: str, root: TreeNode | None):
    print(f"{name}: ", end="")

    if not root:
        print()
        return

    q: deque[TreeNode] = deque()
    q.append(root)
    # print(f"push: root={root.val}")

    while len(q):
        curr = q.popleft()
        print(curr.val, end=", ")

        if curr.left:
            # print(f"push: curr.left={curr.left.val}")
            q.append(curr.left)
        if curr.right:
            # print(f"push: curr.right={curr.right.val}")
            q.append(curr.right)

    print()


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        二分木のルートが渡されます。反転させてそのルートを返します。

        再起的にこノードを呼び出し、後行順巡回 (Post-order Traversal) しながら
        左右の子ノードを入れ替えます。

        #Tree
        #BinaryTree
        #TreeTraversal
        #DFS

        Time complexity: O(n)
        Space complexity: O(h) (height of the tree)

        Args:
            root (TreeNode | None): 二分木のルートを指定します。

        Returns:
            TreeNode | None: 反転した二分木のルートを返します。
        """

        def post_order(node: TreeNode | None):
            if not node:
                return
            post_order(node.left)
            post_order(node.right)
            # print(
            #     f"left={node.left.val if node.left else ''}, right={node.right.val if node.right else ''}"
            # )
            node.left, node.right = node.right, node.left

        post_order(root)

        return root


sol = Solution()
root = create_tree(list=[4, 2, 7, 1, 3, 6, 9])
print_tree("root", root)
ret = sol.invertTree(root)
print_tree("ret", ret)
