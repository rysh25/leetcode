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


def print_tree(name: str, root: TreeNode | None):
    from collections import deque

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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        バイナリツリーのルートを指定すると、そのノードの順序走査した (inorder traversal) 値を返します。

        - Time complexity: O(n)
        - Space complexity: O(h)

        #DFS

        Args:
            root (TreeNode | None): バイナリツリーのルートノード

        Returns:
            list[int]: 順序走査した (inorder traversal) 値を返します。
        """

        def dfs(node: TreeNode | None, routes: list[int]) -> list[int]:
            if node is None:
                return routes

            dfs(node.left, routes)
            if node.val is not None:
                routes.append(node.val)
            dfs(node.right, routes)
            return routes

        return dfs(root, [])


sol = Solution()
root = create_tree([1, None, 2, 3])
print(sol.inorderTraversal(root=root))
root = create_tree([])
print(sol.inorderTraversal(root=root))
root = create_tree([1])
print(sol.inorderTraversal(root=root))
