class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        """
        正の整数の配列 nums と正の整数 k が与えられます。

        nums のサブセットは、絶対差が k に等しい 2 つの整数を含まない場合に美しくなります。

        配列 nums の空ではない美しいサブセットの数を返します。


        nums を昇順に並べ替える。
        バックトラッキングで nums のサブセットを全て生成する。
        nums サブセットに追加した数値を表す配列 count を初期値0で用意する。
        サブセットに、nums[i] を追加する際に、nums[i] - k が1以上であれば
        美しいくならないので、追加しないでバックトラッキングをする。
        (昇順で並べておくことで num[i]-k だけ調べれば良くなる)
        存在しない場合、追加する/しないの2パターンでバックトラッキングをする。
        追加する際は、count[nums[i]] をインクリメントする。
        そうすることで、最後にサブセットが美しいか判断する必要がなくなるため高速化できる。

        - Time complexity: O(2^n)
        - Space complexity: O(n)

        #BackTracking

        Args:
            nums (list[int]): 正の整数の配列
            k (int): 正の整数

        Returns:
            int: 配列 nums の空ではない美しいサブセットの数を返します。
        """

        def backtrack(i: int, curr: list[int], count: list[int]) -> int:
            if i == len(nums):
                # print(f"curr={curr}")
                if len(curr) == 0:
                    return 0
                return 1

            # print(
            #     f"i={i}, nums[i]={nums[i]}, curr={curr}, nums[i] - k in count={nums[i] - k in count}"
            # )

            ret = 0
            if count[nums[i] - k] == 0:
                curr.append(nums[i])
                count[nums[i]] += 1
                ret += backtrack(i + 1, curr, count)

                curr.pop()
                count[nums[i]] -= 1
                ret += backtrack(i + 1, curr, count)
            else:
                ret += backtrack(i + 1, curr, count)

            return ret

        nums.sort()
        count = [0] * 1001
        return backtrack(0, [], count)


sol = Solution()
print(sol.beautifulSubsets(nums=[2, 4, 6], k=2))
print(sol.beautifulSubsets(nums=[1], k=1))
