# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def __init__(self) -> None:
#         pass

#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """

#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """

#     def getList(self) -> [NestedInteger]:
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatten_nested_list = []

        def flatten(nestedList: [NestedInteger]):
            # print(f"flatten:")
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    # print(f"flatten: {nestedList[i].getInteger()}")
                    self.flatten_nested_list.append(nestedList[i].getInteger())
                else:
                    flatten(nestedList[i].getList())

        flatten(nestedList)
        self.index = 0

    def next(self) -> int:
        res = self.flatten_nested_list[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        if len(self.flatten_nested_list) <= self.index:
            return False
        else:
            return True


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext():
#     v.append(i.next())
