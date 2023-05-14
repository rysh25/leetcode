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


class Solution_BFS:
    def maxDepth(self, root: TreeNode | None) -> int:
        """与えられたツリーの深さを数えて返します。

        BFS で深さを数えます。

        Time complexity: O(n)
        Space complexity: O(h) (height of the tree)

        #Tree
        #BinaryTree
        #TreeTraversal
        #BFS

        Args:
            root (TreeNode | None): 深さを数えるツリーを指定します。

        Returns:
            int: 深さを返します。
        """

        if not root:
            return 0

        q: deque[TreeNode] = deque()  # (TreeNode, depth)
        q.append(root)

        level = 0
        while len(q):
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1

        return level


class Solution_IDFS:
    def maxDepth(self, root: TreeNode | None) -> int:
        """与えられたツリーの深さを数えて返します。

        Iterative DFS で深さを数えます。

        Time complexity: O(n)
        Space complexity: O(h) (height of the tree)

        #Tree
        #BinaryTree
        #TreeTraversal
        #DFS

        Args:
            root (TreeNode | None): 深さを数えるツリーを指定します。

        Returns:
            int: 深さを返します。
        """
        if not root:
            return 0

        stack: list[tuple[TreeNode, int]] = []  # (TreeNode, depth)
        stack.append((root, 1))

        max_depth = 0
        while stack:
            node, depth = stack.pop()

            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        指定された2つのツリーが同じかどうかを調べます。

        構造と値が同じであれば同じツリーであると判断します。

        再帰で値と構造が同じであるかを調べます。

        Time complexity: O(n)
        Space complexity: O(n)

        #Tree
        #BinaryTree
        #TreeTraversal
        #BFS

        Args:
            p (TreeNode | None): 同じであるかを調べるツリーを指定します。
            q (TreeNode | None): 同じであるかを調べるツリーを指定します。

        Returns:
            bool: 構造と値が同じであれば True、そうでなければ False を返します。
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False

        return p.val == q.val


sol = Solution()
p = create_tree(list=[1, 2, 3])
q = create_tree(list=[1, 2, 3])
print_tree("p", p)
print_tree("q", q)
print(sol.isSameTree(p, q))


p = create_tree(list=[1, 2])
q = create_tree(list=[1, None, 2])
print_tree("p", p)
print_tree("q", q)
print(sol.isSameTree(p, q))
