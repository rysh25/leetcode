class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        # print(f"\nword={word}, n={n}, k={k}")

        init = word[:k]
        # print(f"init={init}")

        wk = word

        ans = (len(wk) + k - 1) // k
        # print(f"!ans={ans}")
        while len(wk) > k:
            sub = ""
            sublen = 0
            if len(wk) % k == 0:
                sub = wk[-k:]
                sublen = k
            else:
                sublen = n % k
                sub = wk[-sublen:]

            fullmatch = True
            match = False
            while sublen > 0:
                wk = wk[: len(wk) - sublen]
                # print(
                #     f"wk={wk}, sub={sub}, sublen={sublen}, sub[-sublen:]={sub[-sublen:]}, init[:sublen]={init[:sublen]}"
                # )
                if sub[-sublen:] == init[:sublen]:
                    ans = (len(wk) + k - 1) // k
                    match = True
                    # print(f"!match: ans={ans}")
                    if sublen != k:
                        fullmatch = False
                    break
                else:
                    fullmatch = False
                    sublen -= 1

            # print(f"match={match}, fullmatch={fullmatch}, sub={sub}, wk={wk}")
            break
            # if not match:
            #     # print(f"!not match: ans={ans}")
            #     break
            # elif not fullmatch:
            #     break

        return ans


sol = Solution()
print(sol.minimumTimeToInitialState(word="abacaba", k=3))
# print(sol.minimumTimeToInitialState(word="abacabza", k=3))
# print(sol.minimumTimeToInitialState(word="abacaba", k=3))
print(sol.minimumTimeToInitialState(word="abacaba", k=4))
print(sol.minimumTimeToInitialState(word="abcbabcd", k=2))
print(sol.minimumTimeToInitialState(word="aa", k=1))  # 1
print(sol.minimumTimeToInitialState(word="abaa", k=1))  # 3
