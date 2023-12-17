import heapq
from collections import defaultdict


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisine_rating: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)
        self.food_cuisine_map: dict[str, str] = {}
        self.foot_rating: defaultdict[str, int] = defaultdict(int)

        for i in range(len(foods)):
            self.food_cuisine_map[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_rating[cuisines[i]], (-ratings[i], foods[i]))
            self.foot_rating[foods[i]] = -ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine_map[food]
        heapq.heappush(self.cuisine_rating[cuisine], (-newRating, food))
        self.foot_rating[food] = -newRating

    def highestRated(self, cuisine: str) -> str:
        food = ""
        while len(self.cuisine_rating[cuisine]) > 0:
            curr = self.cuisine_rating[cuisine][0]
            if curr[0] != self.foot_rating[curr[1]]:
                heapq.heappop(self.cuisine_rating[cuisine])
                continue
            food = curr[1]
            break
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
