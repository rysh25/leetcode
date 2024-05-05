# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):  # type: ignore
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # This question is bad
        node.val = node.next.val  # type: ignore
        node.next = node.next.next  # type: ignore
