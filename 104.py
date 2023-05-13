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


def createTree(list: list[int | None]):
    if not list:
        return

    root = TreeNode(list[0])
    parent = root
    q: deque[TreeNode] = deque()
    q.append(root)
    i = 1
    while len(q):
        parent = q.popleft()
        if i < len(list):
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.append(node)
            parent.left = node
        i += 1
        if i < len(list):
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.append(node)
            parent.right = node
        i += 1

    return root


def printTree(name: str, root: TreeNode | None):
    if not root:
        return

    print(f"{name}: ", end="")
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
    def maxDepth(self, root: TreeNode | None) -> int:
        """与えられたツリーの深さを数えて返します。

        再起的に子ノードを呼び出します。子供の子ノードの大きい方に1を加えて返します。

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

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


sol = Solution_IDFS()
root = createTree(list=[3, 9, 20, None, None, 15, 7])
printTree("root", root)
print(sol.maxDepth(root))
