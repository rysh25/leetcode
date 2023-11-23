class Solution:
    def checkArithmeticSubarrays(
        self, nums: list[int], l: list[int], r: list[int]
    ) -> list[bool]:
        """
        数列が少なくとも2つの要素から構成され、連続する2つの要素間の差が同じである場合、
        数列は等差数列と呼ばれる。
        より正式には、すべての有効なiに対してs[i+1] - s[i] == s[1] - s[0]である場合に限り、数列sは等差数列である。

        nums[l[i]], nums[l[i]+1], ... nums[r[i]] の部分配列が
        等差数列を形成するように並べ替えられる場合は真、そうでない場合は偽となる boolean の配列 answer を返す。

        - Time complexity(m * n log n)
        - Space complexity(n)

        Args:
            nums (list[int]): n 個の整数の配列
            l (list[int]): m 個の範囲の問い合わせを表す m 個の整数の配列 l
            r (list[int]): m 個の範囲の問い合わせを表す m 個の整数の配列 r

        Returns:
            list[bool]:  boolean の配列 answer を返す。
        """
        m = len(l)

        ans: list[bool] = []
        for q in range(m):
            seq = nums[l[q] : r[q] + 1]
            seq.sort()
            diff = seq[1] - seq[0]
            print(f"q={q}, diff={diff}")
            flg = False
            for i in range(2, len(seq)):
                if seq[i] - seq[i - 1] != diff:
                    ans.append(False)
                    flg = True
                    break
            if not flg:
                ans.append(True)
        return ans


sol = Solution()
print(sol.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
print(
    sol.checkArithmeticSubarrays(
        nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
        l=[0, 1, 6, 4, 8, 7],
        r=[4, 4, 9, 7, 9, 10],
    )
)
