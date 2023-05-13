from __future__ import annotations

from queue import Queue


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
    q: Queue[TreeNode] = Queue()
    q.put(root)
    i = 1
    while not q.empty():
        parent = q.get()
        if i < len(list):
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.put(node)
            parent.left = node
        i += 1
        if i < len(list):
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.put(node)
            parent.right = node
        i += 1

    return root


def printTree(name: str, root: TreeNode | None):
    if not root:
        return

    print(f"{name}: ", end="")
    q: Queue[TreeNode] = Queue()
    q.put(root)
    # print(f"push: root={root.val}")

    while not q.empty():
        curr = q.get()
        print(curr.val, end=", ")

        if curr.left:
            # print(f"push: curr.left={curr.left.val}")
            q.put(curr.left)
        if curr.right:
            # print(f"push: curr.right={curr.right.val}")
            q.put(curr.right)

    print()


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """与えられたツリーの深さを数えて返します。

        再起的に子ノードを呼び出します。子供の子ノードの大きい方に1を加えて返します。

        Time complexity: O(n)
        Space complexity: O(h) (height of the tree)

        #Tree
        #BinaryTree

        Args:
            root (TreeNode | None): 深さを数えるツリーを指定します。

        Returns:
            int: 深さを返します。
        """

        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


sol = Solution()
root = createTree(list=[3, 9, 20, None, None, 15, 7])
printTree("root", root)
print(sol.maxDepth(root))
