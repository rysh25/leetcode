class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        与えられた整数配列numsについて、最長増加部分列の長さを返します。


        DP を行い lis 配列に最長増加部分列を作成する。
        事前に nums と同じ長さの lis 配列を inf で初期化し用意する。
        nums 配列の順番に処理しながら lis 配列を作成する
        nums[i] を処理する際に、i-1 まで処理する際に作成した lis 配列から、lower bound を二分探索で検索する。
        lis を更新しながら、ans にはこれまで見つけたlis 最長増加部分列の長さを記憶しておく。

        #DP
        #BinarySearch
        #LongestIncreasingSubsequence

        Args:
            nums (list[int]): 整数配列

        Returns:
            int: 最も長い厳密に増加する部分列の長さを返します。
        """
        # print(f"nums={nums}")
        INF = 10**9 + 1
        lis: list[int] = [INF] * len(nums)
        ans = 0
        for x in nums:
            l, r = -1, ans + 1
            # print(f"l={l}, r={r}")
            while r - l > 1:
                m = l + ((r - l) // 2)
                if lis[m] >= x:
                    r = m
                else:
                    l = m
            lis[r] = x
            # print(f"lis={lis}")
            ans = max(r + 1, ans)
        # print(f"lis={lis}")
        return ans


sol = Solution()
print(sol.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
print(sol.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
print(sol.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
