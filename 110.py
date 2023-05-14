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


def printTree(name: str, root: TreeNode | None):
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

        leftHeight = self.calcHeight(node.left)
        rightHeight = self.calcHeight(node.right)

        self.ans = abs(leftHeight - rightHeight) <= 1 if self.ans else self.ans

        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        指定されたツリーが平衡しているかを調べて返します。

        DFS でツリーの高さを求めながら、すべての節で左右の高さの差が1以上あった場合は、
        平衡していると判断します。

        Time complexity: O(n)
        Space complexity: O(n)

        #Tree
        #BinaryTree
        #TreeTraversal
        #DFS

        Args:
            root (TreeNode | None): 平衡しているか判断するツリーを指定します。

        Returns:
            bool: 平衡していれば True、そうでなければ False を返します。
        """
        self.ans = True

        if not root:
            return self.ans

        self.calcHeight(root)

        return self.ans


sol = Solution()
root = createTree(list=[3, 9, 20, None, None, 15, 7])
printTree("root", root)
print(sol.isBalanced(root))


root = createTree(list=[1, 2, 2, 3, 3, None, None, 4, 4])
printTree("root", root)
print(sol.isBalanced(root))

root = createTree(list=[])
printTree("root", root)
print(sol.isBalanced(root))
