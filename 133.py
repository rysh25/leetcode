class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        指定されたグラフのディープコピーを返す。

        Args:
            node (Optional['Node']): グラフ

        Returns:
            Optional['Node']: グラフのディープコピーを返す。
        """
        nodes: dict[int, Node] = {}  # val, Node

        def dfs(n: Node) -> Node:
            # print(f"n={n}")
            new_node = Node(n.val)
            nodes[n.val] = new_node

            for v in n.neighbors:
                if v.val in nodes:
                    new_node.neighbors.append(nodes[v.val])
                else:
                    new_node.neighbors.append(dfs(v))

            return new_node

        if node is None:
            return None

        # print("node={node}")
        return dfs(node)


def create_graph(g: list[list[int]]):
    nodes: list[Node] = []
    for i in range(len(g)):
        node = Node(i + 1, None)
        nodes.append(node)

    for i in range(len(g)):
        for j in range(len(g[i])):
            nodes[i].neighbors.append(nodes[j])

    return Node() if len(nodes) == 0 else nodes[0]


visited: set[int] = set()


def print_graph(g: Optional["Node"], new_new: bool = True):
    if g is None:
        return

    print(g.val, end=" ")
    visited.add(g.val)

    for v in g.neighbors:
        if v.val in visited:
            continue
        print_graph(v, False)

    if new_new:
        print()


sol = Solution()
print_graph(sol.cloneGraph(create_graph([[2, 4], [1, 3], [2, 4], [1, 3]])))
print_graph(sol.cloneGraph(create_graph([[]])))
print_graph(sol.cloneGraph(create_graph([])))
