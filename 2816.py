from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from collections import deque

        if head is None:
            return None

        st: deque[ListNode] = deque()

        curr = head
        while curr:
            st.append(curr)
            curr = curr.next

        carry = 0
        while len(st) > 0:
            curr = st.pop()
            curr.val *= 2
            curr.val += carry
            carry = curr.val // 10
            curr.val %= 10

        if carry > 0:
            new_head = ListNode()
            new_head.val = carry
            new_head.next = head
            head = new_head

        return head
