from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" | None = None):
        self.val: int = val
        self.next: "ListNode" | None = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """
        非負整数からなる2つの空でない連結リストが渡されます。
        数値が逆順で保存されており、各ノードは1桁の数字です。

        2つの数値を足した連結リストを返します。

        Time complexity: O(N)
        Space complexity: O(N)

        #LinkedList

        Args:
            l1 (ListNode | None): 非負整数からなる空でない連結リストを指定します。
            l2 (ListNode | None): 非負整数からなる空でない連結リストを指定します。

        Returns:
            ListNode | None: 2つのリストの対応する要素の数値を足した連結リストを返します。
        """

        carry = 0

        dummy = ListNode(0, None)
        prev = dummy

        while l1 or l2:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next

            carry = 1 if num > 9 else 0
            num = num % 10 if num > 9 else num

            tmp = ListNode(num, None)
            prev.next = tmp
            prev = prev.next

        if carry:
            tmp = ListNode(carry, None)
            prev.next = tmp
            prev = prev.next

        return dummy.next


def createLinkedList(list: list[int]) -> ListNode | None:
    dummy = ListNode(0, None)
    prev = dummy
    for i in list:
        tmp = ListNode(i, None)
        prev.next = tmp
        prev = prev.next
    return dummy.next


def printLinkedList(s: str, list: ListNode | None):
    print(f"{s}: [", end="")
    curr = list
    while curr:
        print(curr.val, end=", ")
        curr = curr.next
    print("]")


sol = Solution()
l1 = createLinkedList(list=[9, 9, 9, 9, 9, 9, 9])
printLinkedList("l1", l1)

l2 = createLinkedList(list=[9, 9, 9, 9])
printLinkedList("l2", l2)

ret = sol.addTwoNumbers(l1, l2)
printLinkedList("ret", ret)
