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


class Solution_BFS:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        """
        root に指定された二分探索木の閉区間 [low, height] の値のすべてのノードの
        合計を返します。

        BFS ですべてのノードを訪問し、指定の範囲内であれば、値を合計値に足します。

        Time complexity: O(n)
        Space complexity: O(n)

        #Tree
        #BinaryTree
        #BinarySearchTree
        #TreeTraversal
        #BFS

        Args:
            root (TreeNode | None): 二分探索木
            low (int): 検索する最小値を指定します。
            high (int): 検索する最大値を指定します。

        Returns:
            int: 合計を返します。
        """
        if not root:
            return 0

        q: deque[TreeNode] = deque()
        q.append(root)

        ans = 0

        while len(q):
            node = q.popleft()

            if node.val and low <= node.val <= high:
                ans += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        """
        root に指定された二分探索木の閉区間 [low, height] の値のすべてのノードの
        合計を返します。

        二分探索木 (Binary Search Tree: BST) は、各ノードの子ノードが最大2つであり、
        左ノードの子孫の各値全てが小さく、右ノードの子孫の各値全てが大きいという制約を持つツリーのことです。

        DFS ですべてのノードを訪問し、指定の範囲内であれば、値を合計値に足します。
        ただし、BST であるため low より小さい値の左と、hight より大きい値の右は訪問しないものとします。

        Time complexity: O(n)
        Space complexity: O(n)

        #Tree
        #BinaryTree
        #BinarySearchTree
        #TreeTraversal
        #DFS

        Args:
            root (TreeNode | None): 二分探索木
            low (int): 検索する最小値を指定します。
            high (int): 検索する最大値を指定します。

        Returns:
            int: 合計を返します。
        """
        if not root or not root.val:
            return 0

        if low <= root.val <= high:
            return (
                self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
                + root.val
            )
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return 0


sol = Solution()
root = create_tree([10, 5, 15, 3, 7, None, 18])
print(sol.rangeSumBST(root=root, low=7, high=15))
root = create_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
print(sol.rangeSumBST(root=root, low=6, high=10))
