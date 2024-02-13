class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        n = len(words)
        oln = 0  # number of odd length words
        eln = 0  # number of even length words

        letters: list[int] = [0] * 26
        olln = 0  # number of odd number of letters
        elln = 0  # number of even number of letters

        lc = 0  # letter count
        elc = 0  # even number letter count

        x: list[int] = [
            0
        ] * n  # 各文字列で、必要な2個ペアの数(偶数文字列の数/2 + 奇数文字列/2)
        z = 0  # 2個ペアの数

        for i in range(n):
            x[i] += len(words[i]) // 2
            if len(words[i]) % 2 == 0:
                eln += 1
            else:
                oln += 1

            for j in range(len(words[i])):
                lc += 1
                letters[ord(words[i][j]) - ord("a")] += 1

        for j in range(len(letters)):
            z += letters[j] // 2
            if letters[j] == 0:
                continue
            if letters[j] % 2 == 0:
                elc += letters[j]
                elln += 1
            else:
                olln += 1

        # print(f"n={n}, oln={oln}, eln={eln}, words={words}")
        # print(f"olln={olln}, elln={elln}, lc={lc}, elc={elc}")

        # print(f"lc-oln={lc-oln}")
        x.sort()  # 必要な2個ペアの数が少ない順にソートする
        # print(f"x={x},z={z}")

        ans = 0  # 回文が成り立つ文字列の数
        for i in range(n):
            if x[i] <= z:
                z -= x[i]
                ans += 1

        # odd = min(oln, olln)
        return ans


sol = Solution()
print(sol.maxPalindromesAfterOperations(words=["abbb", "ba", "aa"]))
print(sol.maxPalindromesAfterOperations(words=["abc", "ab"]))
print(sol.maxPalindromesAfterOperations(words=["cd", "ef", "a"]))
