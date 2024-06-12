class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quicksort(arr: list[int], low: int, high: int):
            if low < high:
                pi = partition(arr, low, high)
                quicksort(arr, low, pi - 1)
                quicksort(arr, pi + 1, high)

        def partition(arr: list[int], low: int, high: int):
            pivot = arr[high]
            i = low - 1
            # print(f"arr={arr}")
            for j in range(low, high):
                # print(f"i={i}, j={j}, arr[j]={arr[j]}, pivot={pivot}")
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            # print(f"i={i}, high={high}, arr={arr}")
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            # print(f"arr={arr}")
            return i + 1

        n = len(nums)
        quicksort(nums, 0, n - 1)


sol = Solution()
# print(sol.sortColors(nums=[2, 0, 2, 1, 1, 5]))
print(sol.sortColors(nums=[2, 5, 1, 4, 3, 2]))
# print(sol.sortColors(nums=[2, 0, 1]))
