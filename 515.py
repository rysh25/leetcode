from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int | None = 0,
        left: "TreeNode" | None = None,
        right: "TreeNode" | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        """
        バイナリーツリーのルートが与えられる。
        ツリーの各行の最大値の配列を返す。


        BFS で各ノードをトラバースしながら現在の行の最大値をリストに記録する。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #BinaryTree
        #BFS

        Args:
            root (TreeNode | None): バイナリーツリーのルートが与えられる。

        Returns:
            list[int]: ツリーの各行の最大値の配列を返す。
        """
        ans: list[int] = []

        q: deque[tuple[TreeNode, int]] = deque()

        if not root:
            return ans

        q.append((root, 0))

        while q:
            curr, row = q.pop()

            if curr.val is not None and len(ans) <= row:
                ans.append(curr.val)
            elif curr.val is not None:
                ans[row] = max(ans[row], curr.val)

            if curr.left:
                q.append((curr.left, row + 1))

            if curr.right:
                q.append((curr.right, row + 1))

        return ans


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


sol = Solution()
root = create_tree(list=[1, 3, 2, 5, 3, None, 9])
print_tree("root", root)
print(sol.largestValues(root=root))

root = create_tree(list=[1, 2, 3])
print_tree("root", root)
print(sol.largestValues(root=root))


root = create_tree(list=[0])
print_tree("root", root)
print(sol.largestValues(root=root))
