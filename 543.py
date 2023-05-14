from __future__ import annotations

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int | None = 0,
        left: TreeNode | None | None = None,
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
        if i < len(list) and list[i]:
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.append(node)
            parent.left = node
        i += 1
        if i < len(list) and list[i]:
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
    def calcHeight(self, node: TreeNode | None) -> int:
        if not node:
            return 0

        left_height = self.calcHeight(node.left)
        right_height = self.calcHeight(node.right)

        self.ans = max(self.ans, left_height + right_height)

        return max(left_height, right_height) + 1

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        2分木の直径を返します。

        再起的にこノードを呼び出し、しながらツリーの高さを計算します。
        その際、左右の高さを足した値の最大値(直径)を合わせて求めます。

        #Tree
        #BinaryTree
        #TreeTraversal
        #DFS

        Args:
            root (TreeNode | None): 2分木のルートを指定します。

        Returns:
            int: 計算した直径を返します。
        """
        self.ans = 0

        if not root:
            return self.ans

        self.calcHeight(root)

        return self.ans


sol = Solution()
root = create_tree(list=[1, 2, 3, 4, 5])
print_tree("root", root)
print(sol.diameterOfBinaryTree(root))


root = create_tree(list=[1, 2])
print_tree("root", root)
print(sol.diameterOfBinaryTree(root))
