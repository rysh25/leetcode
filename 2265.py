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


class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        """
        バイナリ ツリーのルートを指定すると、
        ノードの値がそのサブツリー内の値の平均に等しいノードの数を返します。

        注記:
        - n 個の要素の平均は、n 個の要素の合計を n で割って、最も近い整数に切り捨てたものです。
        - ルートのサブツリーは、ルートとそのすべての子孫で構成されるツリーです。

        - Time complexity: O(n)
        - Space complexity: O(h): * h はツリーの高さ

        #DFS

        Args:
            root (TreeNode | None): バイナリ ツリーのルート

        Returns:
            int: ノードの値がそのサブツリー内の値の平均に等しいノードの数を返します。
        """
        self.ans = 0

        self.dfs(root)

        return self.ans

    def dfs(self, curr: TreeNode | None) -> tuple[int, int]:
        """
        バイナリツリーのノードを指定すると、そのサブツリーのノードの値の合計と、ノードの数の合計を返します。

        Args:
            curr (TreeNode | None): バイナリツリーのノード

        Returns:
            tuple[int, int]: サブツリーのノードの値の合計と、ノードの数の合計を返します。
        """
        sum = 0
        count = 0

        if curr is None:
            return 0, 0

        if curr.val is not None:
            sum += curr.val
        count += 1

        if curr.left is not None:
            s, c = self.dfs(curr.left)
            sum += s
            count += c

        if curr.right is not None:
            s, c = self.dfs(curr.right)
            sum += s
            count += c

        if curr.val == sum // count:
            self.ans += 1

        return sum, count


sol = Solution()
print(sol.averageOfSubtree(create_tree([4, 8, 5, 0, 1, None, 6])))
print(sol.averageOfSubtree(create_tree([1])))
