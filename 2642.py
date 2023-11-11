class Graph:
    """
    #Graph
    #FloydWarshall
    """

    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.INF = 10**18 + 1
        self.costs: list[list[int]] = [[self.INF] * self.n for _ in range(self.n)]

        for i in range(self.n):
            self.costs[i][i] = 0

        for from_v, to_v, cost in edges:
            self.costs[from_v][to_v] = cost

        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    self.costs[j][k] = min(
                        self.costs[j][k], self.costs[j][i] + self.costs[i][k]
                    )

        print(f"costs={self.costs}")

    def addEdge(self, edge: list[int]) -> None:
        from_v, to_v, cost = edge
        for i in range(self.n):
            for j in range(self.n):
                self.costs[i][j] = min(
                    self.costs[i][j],
                    self.costs[i][from_v] + self.costs[to_v][j] + cost,
                )

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.costs[node1][node2] >= self.INF:
            return -1

        return self.costs[node1][node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

obj = Graph(
    n=17,
    edges=[
        [6, 3, 475731],
        [3, 7, 515993],
        [13, 8, 904914],
        [1, 15, 665336],
        [3, 4, 419955],
        [2, 5, 591627],
        [15, 13, 180374],
        [8, 6, 939578],
        [7, 10, 459913],
        [8, 1, 942800],
        [14, 6, 876558],
        [15, 5, 215248],
        [13, 14, 762427],
        [1, 5, 914567],
        [6, 12, 919273],
        [12, 16, 342212],
        [10, 8, 60822],
        [3, 14, 947396],
        [15, 0, 263172],
        [10, 6, 711514],
        [9, 14, 120577],
        [11, 5, 476839],
        [11, 13, 438668],
        [12, 9, 527842],
        [14, 16, 588402],
        [15, 2, 195790],
        [1, 9, 785659],
        [2, 7, 787223],
        [11, 7, 99316],
        [6, 1, 948004],
        [4, 12, 31559],
        [5, 4, 453573],
        [5, 8, 141131],
        [5, 12, 767697],
        [1, 12, 312956],
        [14, 11, 374561],
        [15, 11, 19433],
        [0, 9, 227239],
        [12, 10, 325409],
        [16, 13, 413278],
        [10, 1, 155788],
        [5, 3, 294209],
        [7, 5, 54490],
        [3, 13, 701716],
        [2, 8, 927178],
        [12, 14, 367956],
        [14, 10, 953761],
        [3, 16, 9061],
        [2, 3, 421223],
        [4, 15, 189155],
        [14, 2, 711954],
        [16, 15, 734202],
        [7, 4, 917325],
        [0, 1, 818496],
        [8, 3, 548282],
        [16, 12, 385482],
    ],
)
# obj.addEdge(edge)
param_2 = obj.shortestPath(node1=0, node2=11)
print(param_2)  # 722377
