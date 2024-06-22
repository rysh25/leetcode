class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
         整数配列 nums と整数 k が与えられたとします。
         連続部分配列に k 個の奇数がある場合、その部分配列は nice と呼ばれます。

        nice サブ配列の数を返します。


        odd の数が k である範囲をスライディングウィンドウで、その中の nice である部分配列の数を足す。
        範囲内の nice である部分配列の数は、odd の数が変わらない部分配列の数のため、l から odd の数が変わらない範囲までの数となる。

        - Time complexity: O(n)
        - Space complexity: O(k)

        #SlidingWindow

        Args:
            nums (list[int]): 整数配列
            k (int): 整数

        Returns:
            int: nice サブ配列の数を返します。
        """
        from collections import deque

        l = 0
        count = 0
        ans = 0
        r_hist: deque[int] = deque()
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                r_hist.append(r)
                count += 1

            while count > k:
                if nums[l] % 2 == 1:
                    l += 1
                    if l > r_hist[0]:
                        r_hist.popleft()
                    count -= 1
                else:
                    l += 1

            # print(f"l={l}, r={r}, r_hist[0]={r_hist[0]}, count={count}, ans={ans}")

            if count == k:
                ans += r_hist[0] - l + 1

        return ans


sol = Solution()
print(sol.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
print(sol.numberOfSubarrays(nums=[2, 4, 6], k=1))
print(sol.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
print(sol.numberOfSubarrays(nums=[2044, 96397, 50143], k=1))
print(
    sol.numberOfSubarrays(
        nums=[
            91473,  # o
            45388,
            24720,
            35841,  # o
            29648,
            77363,  # o
            86290,
            58032,
            53752,
            87188,
            34428,
            85343,  # o
            19801,  # o
            73201,  # o
        ],
        k=4,
    )  # 6
)
