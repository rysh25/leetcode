class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        与えられたのは、peopleという配列で、
        people[i]はi番目の人の体重を表します。また、limit を最大重量として、無限の数のボートがあります。
        各ボートは limit を超えない限り、最大で2人の人を同時に運ぶことができます。

        与えられたすべての人を運ぶために必要な最小のボート数を返します。

        #TwoPointers
        #Greedy

        - Time complexity: O(n log n)
        - Space complexity: O(n)

        Args:
            people (list[int]): people[i]はi番目の人の体重を表します。
            limit (int): 1つのボートで運べる最大重量を表します。

        Returns:
            int: 与えられたすべての人を運ぶために必要な最小のボート数を返します。
        """
        people.sort()

        l, r = 0, len(people) - 1

        print(f"people={people}")

        ans = 0
        while l <= r:
            if l == r:
                l += 1
            elif people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1

            ans += 1

        return ans


sol = Solution()
print(sol.numRescueBoats(people=[1, 2], limit=3))
print(sol.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(sol.numRescueBoats(people=[3, 5, 3, 4], limit=5))
