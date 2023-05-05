from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = None
        while curr:
            print(curr.val)
            prev = ListNode(curr.val, prev)
            curr = curr.next

        return prev


sol = Solution()
n3 = ListNode(3, None)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
ret = sol.reverseList(n1)

curr = ret
while curr:
    print(curr.val)
    curr = curr.next
