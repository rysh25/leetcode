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
    def dfs(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        """
        subRoot に指定された2分木が root に指定された二分木のサブツリーであれば
        True、そうでなければ False を返します。

        BFS で root のすべてのノードを回りながら、DFS で サブツリーが一致するかを調べます。

        - Time complexity: O(mn)
        - Space complexity: O(m+n)

        m は root ツリーのノード数、n は subRoot ツリーのノード数です。

        #Tree
        #BinaryTree
        #TreeTraversal
        #DFS
        #BFS

        Args:
            root (TreeNode | None): 2分木を指定します。
            subRoot (TreeNode | None): root のサブツリーを指定します。

        Returns:
            bool: subRoot が root のサブツリーであれば True、そうでなければ False を返します。
        """

        if not root and not subRoot:
            return True
        elif root and not subRoot:
            return True
        elif not root:
            return False

        q: deque[TreeNode] = deque()
        q.append(root)
        while len(q):
            node = q.popleft()

            # print(f"node={node.val}")

            if self.dfs(node, subRoot):
                return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False


sol = Solution()

root = create_tree(list=[3, 4, 5, 1, 2])
print_tree("root", root)
subRoot = create_tree(list=[4, 1, 2])
print_tree("subRoot", subRoot)
print(sol.isSubtree(root=root, subRoot=subRoot))


root = create_tree(list=[3, 4, 5, 1, 2, None, None, None, None, 0])
print_tree("root", root)
subRoot = create_tree(list=[4, 1, 2])
print_tree("subRoot", subRoot)
print(sol.isSubtree(root=root, subRoot=subRoot))
