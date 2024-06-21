class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        """
        n分間店を開いている書店のオーナーがいます。
        毎分、何人かの顧客が店に入ってきます。
        長さ n の整数配列 customer が与えられます。ここで、customers[i] は、i 分の開始時に店舗に入店し、その分の終了後にすべての顧客が退店する顧客の番号です。

        本屋の店主が不機嫌になることもあります。バイナリ配列 grumpy が与えられます。
        ここで、本屋のオーナーが i 分間不機嫌であれば grumpy[i] は 1、それ以外の場合は 0 になります。

        書店主が不機嫌なときはその分の客は満足しないが、そうでなければ満足する。

        本屋の店主は、minutes 分間連続して不機嫌にならないための秘密のテクニックを知っていますが、それを使えるのは 1 回だけです。

        1 日を通して満足できる顧客の最大数を返します。


        店主が不機嫌でない時間に訪れる顧客の数と、minues 分間で店主が不機嫌な間に訪れる最大値を求める。
        店主が不機嫌でない時間に訪れる顧客の数からminues 分間で店主が不機嫌な間に訪れる最大値を引いたものが答えになる。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #SlidingWindow

        Args:
            customers (list[int]): 顧客の入店時間を表す整数配列
            grumpy (list[int]): 本屋の店主が不機嫌になる時間を表すバイナリ配列
            minutes (int): 不機嫌にならない時間

        Returns:
            int: 1 日を通して満足できる顧客の最大数を返します。
        """

        n = len(customers)
        sum = 0
        curr = 0
        l = 0
        mx = 0
        for r in range(n):
            if grumpy[r]:
                curr += customers[r]
            else:
                sum += customers[r]

            if r - l >= minutes:
                if grumpy[l]:
                    curr -= customers[l]
                l += 1

            mx = max(mx, curr)

        # print(f"sum={sum}, mx={mx}")

        return sum + mx


sol = Solution()
print(
    sol.maxSatisfied(
        customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3
    )
)
print(sol.maxSatisfied(customers=[1], grumpy=[0], minutes=1))
print(sol.maxSatisfied(customers=[2, 6, 6, 9], grumpy=[0, 0, 1, 1], minutes=1))  # 17
