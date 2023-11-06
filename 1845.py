import heapq


class SeatManager:
    def __init__(self, n: int):
        self.available_seats: list[int] = list(range(1, n + 1))
        heapq.heapify(self.available_seats)

    def reserve(self) -> int:
        if self.available_seats:
            return heapq.heappop(self.available_seats)
        return -1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
n = 5
obj = SeatManager(n)
param_1 = obj.reserve()
print(param_1)
seatNumber = param_1
obj.unreserve(seatNumber)
