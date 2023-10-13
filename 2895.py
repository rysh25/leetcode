class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        # print(f"processorTime={processorTime}, tasks={tasks}")
        n = len(processorTime)
        processorTime.sort()
        tasks.sort(reverse=True)
        # print(f"processorTime={processorTime}, tasks={tasks}")
        max_time = 0

        for i in range(n):
            task_time = max([processorTime[i] + tasks[4 * i + j] for j in range(4)])
            max_time = max(max_time, task_time)

        return max_time


sol = Solution()
print(sol.minProcessingTime(processorTime=[8, 10], tasks=[2, 2, 3, 1, 8, 7, 4, 5]))
print(sol.minProcessingTime(processorTime=[10, 20], tasks=[2, 3, 1, 2, 5, 8, 4, 3]))
