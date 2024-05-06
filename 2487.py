# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: ListNode|None) -> ListNode|None:
        from collections import deque
        st: deque[ListNode] = []

        curr = head

        while curr is not None:
            while len(st) > 0 and st[-1].val < curr.val:
                st.pop()

            st.append(curr)

            curr = curr.next

        if len(st) == 0:
            return None
        else:
            head = st[0]

            curr = head

            for i in range(1, len(st)):
                curr.next = st[i]

                curr = st[i]

            curr.next = None


        return head


