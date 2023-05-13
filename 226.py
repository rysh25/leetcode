from __future__ import annotations

from queue import Queue


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
root = createTree(list=[4, 2, 7, 1, 3, 6, 9])
printTree("root", root)
ret = sol.invertTree(root)
printTree("ret", ret)
