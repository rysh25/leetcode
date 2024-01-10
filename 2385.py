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


class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        """
        一意の値を持つバイナリ ツリーの root と整数の start が与えられます。 分 0 で、値 start を持つノードから感染が開始されます。

        次の場合、ノードは毎分感染します。

        ノードは現在感染していません。
        ノードは感染したノードに隣接しています。
        ツリー全体が感染するのに必要な分数を返します。


        まず、BFS で、ツリーの親子関係の関連を graph に記録する
        そして、DFS で start ノードから最長を調べる。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #BFS
        #DFS

        Args:
            root (TreeNode | None): 一意の値を持つバイナリ ツリー
            start (int): 整数

        Returns:
            int: ツリー全体が感染するのに必要な分数を返します。
        """
        from collections import defaultdict, deque

        graph: defaultdict[TreeNode, list[TreeNode]] = defaultdict(list)

        q: deque[tuple[TreeNode, TreeNode | None]] = deque()

        if root is None:
            return 0

        start_node: TreeNode | None = None
        q.append((root, None))

        while q:
            curr, parent = q.popleft()
            # print(
            #     f"q: curr={curr.val}, parent={parent.val if parent is not None else ''}"
            # )

            if curr.val == start:
                start_node = curr

            if parent is not None:
                graph[parent].append(curr)
                graph[curr].append(parent)

            if curr.left is not None:
                q.append((curr.left, curr))
            if curr.right is not None:
                q.append((curr.right, curr))

        visited: set[TreeNode] = set()

        def dfs(node: TreeNode, length: int) -> int:
            # print(f"val={node.val}, length={length}")
            visited.add(node)
            ret = length
            for nv in graph[node]:
                # print(f"node={node.val}: nv={nv.val}")
                if nv and nv not in visited:
                    ret = max(ret, dfs(nv, length + 1))
            return ret

        if start_node is None:
            return 0

        return dfs(start_node, 0)


sol = Solution()
print(sol.amountOfTime(root=create_tree([1, 5, 3, None, 4, 10, 6, 9, 2]), start=3))
print(sol.amountOfTime(root=create_tree([1]), start=3))
print(sol.amountOfTime(root=create_tree([1, 2, None, 3, None, 4, None, 5]), start=1))
print(sol.amountOfTime(root=create_tree([5, 4, 3]), start=5))
print(sol.amountOfTime(root=create_tree([1, None, 2, 3, 4, None, 5]), start=4))
