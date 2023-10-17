from collections import deque


class Solution_BFS:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        """
        0 から n - 1 までの番号が付けられた n 個のバイナリツリーノードがあり、
        ノード i には 2 つの子 leftChild[i] と rightChild[i] があり、
        指定されたすべてのノードが正確に 1 つの有効なバイナリツリーを形成する場合にのみ true を返す。

        ノード i に左の子がない場合、leftChild[i] は -1 になり、右の子の場合も同様

        - Time complixity: O(n)
        - Space complexity: O(n)

        #BFS
        #BinaryTree

        Args:
            n (int): バイナリツリーのノード数
            leftChild (list[int]): バイナリツリーのノードの左の子供を表す配列
            rightChild (list[int]): バイナリツリーのノードの右の子供を表す配列

        Returns:
            bool: 指定されたすべてのノードが正確に 1 つの有効なバイナリツリーを形成する場合にのみ true を返す。
        """
        indegree = [0] * n  # Initialize in-degree of all nodes to 0

        # Build the in-degree array in a single pass
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1

        # Find the root (node with in-degree 0)
        root = None
        for i in range(n):
            if indegree[i] == 0:
                if root is None:
                    root = i
                else:
                    return False  # More than one root

        # If there's no root
        if root is None:
            return False

        visited: set[int] = set()

        q: deque[int] = deque()

        q.append(root)

        while q:
            cn = q.pop()
            if cn in visited:
                return False
            visited.add(cn)

            if leftChild[cn] != -1:
                q.append(leftChild[cn])
            if rightChild[cn] != -1:
                q.append(rightChild[cn])

        return n == len(visited)


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        """
        0 から n - 1 までの番号が付けられた n 個のバイナリツリーノードがあり、
        ノード i には 2 つの子 leftChild[i] と rightChild[i] があり、
        指定されたすべてのノードが正確に 1 つの有効なバイナリツリーを形成する場合にのみ true を返す。

        ノード i に左の子がない場合、leftChild[i] は -1 になり、右の子の場合も同様

        #DFS
        #BinaryTree

        - Time complixity: O(n)
        - Space complexity: O(n)

        Args:
            n (int): バイナリツリーのノード数
            leftChild (list[int]): バイナリツリーのノードの左の子供を表す配列
            rightChild (list[int]): バイナリツリーのノードの右の子供を表す配列

        Returns:
            bool: 指定されたすべてのノードが正確に 1 つの有効なバイナリツリーを形成する場合にのみ true を返す。
        """
        indegree = [0] * n  # Initialize in-degree of all nodes to 0

        # Build the in-degree array in a single pass
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1

        # Find the root (node with in-degree 0)
        root = None
        for i in range(n):
            if indegree[i] == 0:
                if root is None:
                    root = i
                else:
                    return False  # More than one root

        # If there's no root
        if root is None:
            return False

        visited: set[int] = set()

        def dfs(i: int) -> bool:
            if i >= n:
                return True

            if i in visited:
                return False

            visited.add(i)

            if leftChild[i] != -1:
                if not dfs(leftChild[i]):
                    return False

            if rightChild[i] != -1:
                if not dfs(rightChild[i]):
                    return False

            return True

        return dfs(root) and len(visited) == n


sol = Solution()
print(
    sol.validateBinaryTreeNodes(
        n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]
    )
)
print(
    sol.validateBinaryTreeNodes(
        n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]
    )
)
print(sol.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))

print(
    sol.validateBinaryTreeNodes(
        n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]
    )
)


print(
    sol.validateBinaryTreeNodes(
        n=6, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1]
    )  # True
)
