class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
        整数の集合 s があり、これには元々 1 から n までのすべての数値が含まれています。
        残念ながら、何らかのエラーにより、 s の数値の 1 つがセット内の別の数値と重複してしまい、その結果、ある数値が繰り返され、別の数値が失われます。

        エラー後のこのセットのデータ状態を表す整数配列 nums が与えられます。

        2 回出現する数値と欠落している数値を検索し、配列の形式で返します。
        
        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            nums (list[int]): 整数の集合

        Returns:
            list[int]: 2 回出現する数値と欠落している数値を検索し、配列の形式で返します。
        """
        from collections import defaultdict
        
        freq: defaultdict[int, int] = defaultdict(int)
        
        
        ans: list[int] = []
        for i in range(len(nums)):
            freq[nums[i]] += 1
            
            if freq[nums[i]] >= 2:
                ans.append(nums[i])
            
        for i in range(len(nums)):
            if freq[i+1] == 0:
                ans.append(i+1)
                
        return ans
            
        
sol = Solution()
print(sol.findErrorNums(nums = [1,2,2,4]))
print(sol.findErrorNums(nums = [1,1]))