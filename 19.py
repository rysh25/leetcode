from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1

        # print(f"count={count}")

        next: Optional[ListNode] = None
        curr = head
        i = 0
        while curr:
            # print(f"count - n + 1={count - n + 1}, i={i}")
            if count - n + 1 == i:
                # print(f"next={i}")
                next = curr
            curr = curr.next
            i += 1

        # print(f"next={next}")

        if count - n - 1 < 0:
            head = next
        else:
            curr = head
            i = 0
            while curr:
                if count - n - 1 == i:
                    curr.next = next
                curr = curr.next
                i += 1

        return head


n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
list1 = ListNode(1, n2)

sol = Solution()
ret = sol.removeNthFromEnd(head=list1, n=2)

print("ret: ")
curr = ret
while curr:
    print(curr.val)
    curr = curr.next


list1 = ListNode(1, None)

sol = Solution()
ret = sol.removeNthFromEnd(head=list1, n=1)

print("ret: ")
curr = ret
while curr:
    print(curr.val)
    curr = curr.next
