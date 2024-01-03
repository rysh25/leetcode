class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """
        銀行内では盗難防止用のセキュリティ装置が作動しています。
        バンクのフロア プランを表す、0 から始まるインデックスのバイナリ文字列配列バンク (m x n 2D 行列) が与えられます。 Bank[i] は、「0」と「1」で構成される i 番目の行を表します。 「0」はセルが空であることを意味し、「1」はセルにセキュリティ装置があることを意味します。

        次の両方の条件が満たされる場合、2 つのセキュリティデバイス間には 1 本のレーザー ビームが存在します。

        - 2 つのデバイスは、r1 と r2 の 2 つの異なる行に配置されています。ここで、r1 < r2。
        - 各行 i (r1 < i < r2) では、i 番目の行にはセキュリティ デバイスはありません。

        レーザービームは独立しています。
        つまり、1 つのビームが他のビームと干渉したり合流したりすることはありません。

        バンク内のレーザー ビームの総数を返します。

        - Time complexity: O(n * m)
        - Space complexity: O(1)

        Args:
            bank (list[str]): バンクのフロア プランを表す、0 から始まるインデックスのバイナリ文字列配列バンク (m x n 2D 行列) が与えられます。

        Returns:
            int: バンク内のレーザー ビームの総数を返します。
        """

        ans = 0
        prev_count = 0
        for r in bank:
            count = 0
            for i in range(len(r)):
                if r[i] == "1":
                    count += 1
            if count > 0:
                if prev_count > 0:
                    ans += prev_count * count
                prev_count = count
        return ans


sol = Solution()
print(sol.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(sol.numberOfBeams(bank=["000", "111", "000"]))
