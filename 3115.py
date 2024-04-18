class Solution:
    def maximumPrimeDifference(self, nums: list[int]) -> int:

        def sieve_of_eratosthenes(n: int) -> list[int]:
            primes: list[bool] = [True] * (n + 1)
            primes[0], primes[1] = False, False
            for i in range(2, int(n**0.5) + 1):
                if primes[i]:
                    for j in range(i**2, n + 1, i):
                        primes[j] = False
            return [num for num, is_prime in enumerate(primes) if is_prime]

        primes = sieve_of_eratosthenes(100)

        mn = 10**9 + 1
        mx = 0
        for p in primes:
            # print(f"p={p}")

            for i in range(len(nums)):
                if nums[i] == p:
                    mn = min(mn, i)
                    mx = max(mx, i)

        return mx - mn


sol = Solution()
print(sol.maximumPrimeDifference(nums=[4, 2, 9, 5, 3]))
print(sol.maximumPrimeDifference(nums=[4, 8, 2, 8]))
