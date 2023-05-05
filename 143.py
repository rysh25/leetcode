from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        forward = head
        prev = None
        length = 0
        while forward:
            length += 1
            prev = ListNode(forward.val, prev)
            forward = forward.next

        tail = prev

        # print("tail: ")
        # curr = tail
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        forward = head
        backward = tail

        curr = forward
        forward = forward.next

        idx = 0
        for i in range(length - 1):
            if not curr or not forward or not backward:
                break
            if i % 2 == 0:
                print(f"1: backward.val={backward.val}")
                curr.next = backward
                backward = backward.next
            else:
                print(f"2: forward.val={forward.val}")
                curr.next = forward
                forward = forward.next
            curr = curr.next
        curr.next = None


sol = Solution()

n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
list1 = ListNode(1, n2)

sol.reorderList(list1)

curr = list1
while curr:
    print(curr.val)
    curr = curr.next
