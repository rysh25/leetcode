from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        """
        n 個のノードを持つバイナリ ツリーの root が与えられます。
        ツリー内の各ノードには、node.val コインがあります。ツリー全体で合計 n 個のコインがあります。

        1 回の移動で、2 つの隣接するノードを選択し、1 つのコインを 1 つのノードから別のノードに移動します。
        移動は、親から子、または子から親へ行われる場合があります。

        すべてのノードにちょうど 1 つのコインを持たせるために必要な最小移動数を返します。


        DFS の post-order で、子供が親にコインを配る (もしくは親から取る)
        その配った(取った)枚数を合計する。

        #Tree
        #DFS

        - Space complexity: O(n)
        - Time complexity: O(n)

        Args:
            root (TreeNode | None): n 個のノードを持つバイナリ ツリー

        Returns:
            int: すべてのノードにちょうど 1 つのコインを持たせるために必要な最小移動数を返します。
        """

        def f(node: TreeNode | None, parent: TreeNode | None) -> int:
            if node is None:
                return 0

            moves = f(node.left, node) + f(node.right, node)
            x = node.val - 1
            # print(f"node.val={node.val}, x={x}")

            if parent is not None:
                parent.val += x

            moves += abs(x)

            return moves

        return f(root, None)
