class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        整数配列 nusm が与えられる。
        1回の操作で、nums の任意の要素を任意の整数に置き換えることができる。
        次の条件が両方とも満たされる時、nums は連続しているとみなされる。

        - すべての要素は一意である
        - 最大の要素と最小の要素の差が nums.length - 1 と等しい

        nums を連続にする最小の操作数を返す。


        最小の値の値+配列の長さ以外の値が置き換えの対象となる。
        その個数を数える。

        まず nums をソートする。
        ソートした配列の0番目を最小の値として、範囲外の数を置き換えの数として数える。
        ただし、1番目以降を最小として、置き換えをした方が置き換え回数が少ない場合があるため、
        スライディングウィンドウで、ソート済み配列を範囲をずらしながら長さを数える。
        その結果置き換え対象が最小のものが答えとなる。
        ただし重複する値があった場合、範囲内となってしまうので、nums 配列をユニークにしたものを数える。
        その際、範囲外の個数の計算時は元の配列の大きさを使い数えることに注意する。

        - Time complexity: O(n long n)
        - Space complexity: O(n)

        #SlidingWindow

        Args:
            nums (list[int]): 整数配列 nusm が与えられる。

        Returns:
            int: nums を連続にする最小の操作数を返す。
        """
        unique_nums: list[int] = sorted(set(nums))
        # print(f"nums={nums}, len(nums)={len(nums)}, unique_nums={unique_nums}")
        ans = len(nums)
        r = 0
        for l in range(len(unique_nums)):
            while r < len(unique_nums) and unique_nums[r] < unique_nums[l] + len(nums):
                r += 1

            # print(f"l={l}, r={r}, r-l={r-l}, len(nums)-(r-l)={len(nums) - (r - l)}")
            ans = min(ans, len(nums) - (r - l))

        return ans


sol = Solution()
print(sol.minOperations(nums=[4, 2, 5, 3]))
print(sol.minOperations(nums=[1, 2, 3, 5, 6]))
print(sol.minOperations(nums=[1, 10, 100, 1000]))
print(sol.minOperations(nums=[8, 5, 9, 9, 8, 4]))  # 2
print(sol.minOperations(nums=[41, 33, 29, 33, 35, 26, 47, 24, 18, 28]))  # 5
