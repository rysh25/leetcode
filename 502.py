class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        """
        LeetCode がまもなく IPO を開始するとします。ベンチャー キャピタルに高値で株式を売却するために、LeetCode は IPO 前に資本を増やすプロジェクトに取り組みたいと考えています。
        リソースが限られているため、IPO 前に完了できるプロジェクトは最大で k 個です。最大で k 個のプロジェクトを完了した後、LeetCode が総資本を最大化する最善の方法を設計できるように支援してください。

        n 個のプロジェクトが与えられ、i 番目のプロジェクトには純利益 profits[i] があり、開始するには最小資本 capital[i] が必要です。

        最初は w の資本があります。プロジェクトを完了すると、その純利益が得られ、その利益が総資本に追加されます。

        指定されたプロジェクトから最大で k 個のプロジェクトのリストを選択して最終資本を最大化し、最終的に最大化された資本を返します。

        答えは 32 ビットの符号付き整数に収まることが保証されています。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #Greedy

        Args:
            k (int): 指定されたプロジェクトから最大で k 個のプロジェクトのリストを選択する
            w (int): 最初の資本
            profits (list[int]): i 番目のプロジェクトの純利益
            capital (list[int]): i 番目のプロジェクト開始するための最小資本

        Returns:
            int: 最終的に最大化された資本を返します。
        """
        import heapq

        # print(f"capital={capital}")
        # print(f"profits={profits}")
        n = len(profits)

        projects = [[c, p] for c, p in zip(capital, profits)]
        # print(f"projects={projects}")
        projects.sort(key=lambda x: x[0])
        # print(f"projects={projects}")

        count = 0
        ans = w
        pq: list[int] = []
        heapq.heapify(pq)

        i = 0
        while count < k:
            # print(f"k={k}, count={count}, ans={ans}, projects[i]={projects[i]}")
            while i < n and ans >= projects[i][0]:
                heapq.heappush(pq, -projects[i][1])
                i += 1

            # print(f"i={i}")
            if len(pq) == 0:
                break

            count += 1
            ans += -heapq.heappop(pq)

        return ans


sol = Solution()
print(sol.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
print(sol.findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
print(sol.findMaximizedCapital(k=1, w=0, profits=[1, 2, 3], capital=[1, 1, 2]))  # 0
