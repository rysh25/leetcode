class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        """
        サイズ n の整数配列 pref が与えられる。
        次を満たすサイズ n の配列 arr を返す。

        - pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]


        A ^ B は、さらに、A で XOR すると元に戻る。

        Args:
            pref (list[int]): サイズ n の整数配列 pref が与えられる。

        Returns:
            list[int]: サイズ n の配列 arr を返す。
        """

        n = len(pref)
        arr: list[int] = []

        prev = 0
        for i in range(n):
            arr.append(prev ^ pref[i])
            prev = pref[i]

        return arr


sol = Solution()
print(sol.findArray(pref=[5, 2, 0, 3, 1]))
print(sol.findArray(pref=[13]))
