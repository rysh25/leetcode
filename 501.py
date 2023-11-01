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


from collections import defaultdict


class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        """
        重複のある二分探索木 (BST) のルートを指定されます。
        その中のすべてのモード (つまり、最も頻繁に出現する要素) を返します。

        ツリーに複数のモードがある場合は、それらを任意の順序で返します。

        BST が次のように定義されていると仮定します。

        - ノードの左側のサブツリーには、ノードのキー以下のキーを持つノードのみが含まれます。
        - ノードの右側のサブツリーには、ノードのキー以上のキーを持つノードのみが含まれます。
        - 左右のサブツリーも両方とも二分探索ツリーでなければなりません。


        #DFS

        Args:
            root (TreeNode | None): 重複のある二分探索木 (BST) のルートを指定されます。

        Returns:
            list[int]: その中のすべてのモードを返します。
        """
        counter: defaultdict[int, int] = defaultdict(int)
        stack: list[TreeNode] = []

        if not root:
            return []

        stack.append(root)

        while stack:
            curr = stack.pop()

            if not curr:
                continue

            if curr.val is not None:
                counter[curr.val] += 1

            if curr.left is not None:
                stack.append(curr.left)

            if curr.right is not None:
                stack.append(curr.right)

        max_val = max(counter.values())

        ans: list[int] = []

        for key in counter:
            if counter[key] == max_val:
                ans.append(key)

        return ans


sol = Solution()
print(sol.findMode(root=create_tree([1, None, 2, 2])))
print(sol.findMode(root=create_tree([0])))
