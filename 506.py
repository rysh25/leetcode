class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]

        sorted_scores = sorted(score, reverse=True)
        score_dict = {v: i for i, v in enumerate(sorted_scores)}

        # print(f"score_dict={score_dict}")

        ans: list[str] = []
        for s in score:
            # print(f"s={s}")
            rank = score_dict[s]
            if rank < len(medals):
                ans.append(medals[rank])
            else:
                ans.append(str(rank+1))
        return ans

sol = Solution()
print(sol.findRelativeRanks([5,4,3,2,1]))
print(sol.findRelativeRanks([10,3,8,9,4]))
