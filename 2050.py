from collections import deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        """
        整数 n が与えられる。これは 1 から n にラベル付けされた n コースあることを示す。
        2次元整数配列 relations も与えられる。ここで、relations[j] = [prevCourse_j, nextCourse_j] は、
        コース prevCourse_j がコース nextCourse_j の前に完了する必要があることを示す。
        さらに、0 から始まる整数配列 time が与えられる。ここで、time[i] は、(i+1) 番目のコースを完了するのにかかる月数を示します。

        次のルールに従って、すべてのコースを完了するために必要な最小月数を見つける。

        - 前提条件が満たされていれば、いつでもコースの受講を開始できる。
        - 同時に何講座でも受講可能

        すべてのコースを完了するのに必要な最小月数を返す。
        テスト ケースは、すべてのコースを完了できるように生成される (つまり、グラフは有向非巡回グラフです)。

        - Time complexity: O(n + len(relations))
        - Space comlexity: O(n)

        #TopologicalSort

        Args:
            n (int): n コース
            relations (list[list[int]]): _description_
            time (list[int]): _description_

        Returns:
            int: すべてのコースを完了するのに必要な最小月数を返す。
        """

        graph: list[list[int]] = [[] for _ in range(n)]
        indegree: list[int] = [0] * n
        for rel in relations:
            indegree[rel[1] - 1] += 1
            graph[rel[0] - 1].append(rel[1] - 1)

        q: deque[int] = deque()
        for i, node in enumerate(indegree):
            if node == 0:
                q.append(i)

        max_time = time[:]
        while q:
            cn = q.popleft()
            # print(f"cn={cn}")

            for nn in graph[cn]:
                # print(f"nn={nn}, time[cn]={time[cn]}")
                max_time[nn] = max(max_time[nn], max_time[cn] + time[nn])
                indegree[nn] -= 1
                if indegree[nn] == 0:
                    q.append(nn)

        return max(max_time)


sol = Solution()
print(sol.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
print(
    sol.minimumTime(
        n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]
    )
)

print(sol.minimumTime(n=2, relations=[], time=[3, 5]))  # 5
