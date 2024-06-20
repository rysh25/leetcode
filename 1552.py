class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        """
        Earth C-137 の宇宙で、Rick は、新しく発明したバスケットに 2 つのボールを入れると、それらの間に特殊な磁力が発生することを発見しました。
        Rick は n 個の空のバスケットがを持ち、i 番目のバスケットは position[i] にあります。
        Morty は m 個のボールを持ち、任意の 2 つのボール間の最小磁力が最大になるようにボールをバスケットに分配する必要があります。

        Rick は、位置 x と y にある 2 つの異なるボール間の磁力は |x - y| であると述べました。

        整数配列の位置と整数 m が与えられます。必要な磁力を返します。


        ボールの間隔をできるだけ大きくするために、ボールの間隔を2分探索する。
        position をソートし、2分探索で、指定された間隔にボールが m 個のボールが入らなければ
        その間隔より少ない間隔が正解となる。

        - Time complexity: O(n log in)
        - Space complexity: O(1)

        Args:
            position (list[int]): バスケット
            m (int): ボールの数

        Returns:
            int: 必要な磁力を返します。
        """

        position.sort()
        # print(f"position={position}, m={m}")
        l, r = 0, position[-1] - position[0] + 1

        # print(f"l={l}, r={r}")

        while r - l > 1:
            mid = l + (r - l) // 2

            balls = 1
            prev = 0
            for i in range(1, len(position)):
                if position[i] - position[prev] >= mid:
                    prev = i
                    balls += 1

            # print(f"mid={mid}, balls={balls}, m={m}")
            if balls < m:
                r = mid
            else:
                l = mid

        return l


sol = Solution()
print(sol.maxDistance(position=[1, 2, 3, 4, 7], m=3))
print(sol.maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))
print(sol.maxDistance(position=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], m=4))  # 3
