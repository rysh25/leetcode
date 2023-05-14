class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        """
        ランレングス圧縮された int の配列が指定されます。

        freq と num のペアを解凍したリストを返します。

        Time complexity: O(n)
        Space complexity: O(n)

        #RunLengthEncoding

        Args:
            nums (list[int]): ランレングス圧縮された int の配列を指定します。

        Returns:
            list[int]: 解凍した配列を返します。
        """
        ans: list[int] = []

        for i in range(len(nums) // 2):
            freq, num = nums[2 * i], nums[2 * i + 1]
            ans += [num] * freq

        return ans


sol = Solution()
print(sol.decompressRLElist(nums=[1, 2, 3, 4]))
print(sol.decompressRLElist(nums=[1, 1, 2, 3]))
