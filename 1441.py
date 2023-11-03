class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        """
        整数配列と target と、整数 n が与えられます。
        次の2つの操作を持つからのスタックを持っています。

        - "Push": 整数をスタックの一番上にプッシュします。
        - "Pop": スタックの一番上の整数を削除します。

        [1, n] の範囲の整数のストリームもあります。

        2 つのスタック操作を使用して、スタック内の数値 (下から上まで) をターゲットと等しくします。
        次のルールに従う必要があります。

        - 整数のストリームが空でない場合は、ストリームから次の整数を選択し、それをスタックの先頭にプッシュします。
        - スタックが空でない場合は、スタックの先頭にある整数をポップします。
        - スタック内の要素 (下から上まで) がターゲットと等しい場合は、ストリームから新しい整数を読み取らず、スタック上でそれ以上の操作を実行しません。

        前述のルールに従ってターゲットを構築するために必要なスタック操作を返します。 有効な回答が複数ある場合は、いずれかを返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            target (list[int]): 整数配列
            n (int): 整数

        Returns:
            list[str]: ターゲットを構築するために必要なスタック操作を返します。
        """
        ans: list[str] = []
        i = 0

        for num in target:
            print(f"num={num}")
            while i < num - 1:
                ans.append("Push")
                ans.append("Pop")
                i += 1

            ans.append("Push")
            i += 1

        return ans


sol = Solution()
print(sol.buildArray(target=[1, 3], n=3))
print(sol.buildArray(target=[1, 2, 3], n=3))
print(sol.buildArray(target=[1, 2], n=4))
print(sol.buildArray(target=[2, 3, 4], n=4))
print(sol.buildArray(target=[1], n=2))
