class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        """
        0インデックスの整数配列 nums と整数 k が与えられる。
        部分配列 (i, j) のスコアは、min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) と定義される。
        i <= k <= j である部分配列は良い部分配列はである。

        良い部分配列の最大のスコアを返す。


        ある要素が最小値であるとき、範囲はできるだけ広い方がスコアは大きくなる。
        Monotonic Stack で NSL と NSR を使って、各要素を最小値となる範囲をあらかじめ求める。
        その後、各要素について、i <= k <= j を満たす場合、スコアを求めて、その最大値を答えとする。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #Stack
        #MonotonicStack
        #NSL
        #NSR

        Args:
            nums (list[int]): 0インデックスの整数配列
            k (int): 整数 k

        Returns:
            int: 良い部分配列の最大のスコアを返す。
        """
        # print(f"nums={nums}, k={k}")
        n = len(nums)

        def get_nsl_nsr() -> tuple[list[int], list[int]]:
            nsl: list[int] = [0] * n
            nsr: list[int] = [n - 1] * n
            stack: list[int] = []
            for i, num in enumerate(nums):
                nsl[i] = i
                while stack and num <= nums[stack[-1]]:
                    nsr[stack.pop()] = i - 1

                if stack:
                    nsl[i] = stack[-1] + 1
                else:
                    nsl[i] = 0
                stack.append(i)

            return (nsl, nsr)

        nsl, nsr = get_nsl_nsr()
        # print(f"nsl={nsl}")
        # print(f"nsr={nsr}")
        ans = 0
        for i in range(n):
            l = nsl[i]
            r = nsr[i]
            if l <= k <= r:
                ans = max(ans, nums[i] * (r - l + 1))

        return ans


sol = Solution()
print(sol.maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3))
print(sol.maximumScore(nums=[1, 4, 3, 7, 4, 1], k=3))
print(sol.maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0))
print(
    sol.maximumScore(
        nums=[6569, 9667, 3148, 7698, 1622, 2194, 793, 9041, 1670, 1872], k=5
    )
)  # 9732
