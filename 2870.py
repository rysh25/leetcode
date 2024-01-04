class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        minOperations関数は、与えられた正の整数から成る0から始まるインデックスの配列numsを受け取り、
        配列を空にするために必要な最小の操作回数を計算します。

        操作は2つのタイプがあります:
        1. 等しい値を持つ2つの要素を選んで配列から削除する。
        2. 等しい値を持つ3つの要素を選んで削除する。


        nums ないの整数ごとの出現頻度を計算する。
        出現頻度が 1 のものはあった場合は、空にすることができない。
        それ以外の場合は、3で割り切れるなら、なら3を割った商をその整数を消す操作回数とする。
        割り切れないなら、商+1を操作回数とする。あまりが1だとしても、最後の2つを2づつ消すことができるので回数としてはそれで問題ない。
        すべての整数について操作回数を足し合わせたものが答えとなる。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #Greedy

        Args:
            nums (list[int]): 正の整数から成る0から始まるインデックスの配列

        Returns:
            int: 配列を空にするために必要な最小の操作回数。不可能な場合は-1。
        """
        from collections import defaultdict

        freq: defaultdict[int, int] = defaultdict(int)

        for i in nums:
            freq[i] += 1

        ans = 0

        for k in freq:
            count = freq[k]
            if count <= 1:
                return -1
            op, r = divmod(freq[k], 3)
            if r != 0:
                op += 1

            ans += op
        return ans


sol = Solution()
print(sol.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(sol.minOperations(nums=[2, 1, 2, 2, 3, 3]))
