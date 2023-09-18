class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        整数配列 nums が与えられる。もし配列内にいずれかの値が少なくとも2回現れたら、
        true を返す。もしすべての要素が異なるものであれば false を返す。

        各数字が配列の中に2回以上出てくるか調べるために、nums を set に入れて、
        長さが元と変わっているかを調べる。

        Time complexity: O(N)
        Space complexity: O(N)

        #Array
        """
        return len(nums) != len(set(nums))


sol = Solution()
print(sol.containsDuplicate(nums=[1, 2, 3, 4]))
