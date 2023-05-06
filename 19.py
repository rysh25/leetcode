from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        fast、slow ポインターを用意する
        fast ポインターを n 進める
        fast が空なら n = リストの長さのため、head.next を返す。(1つ目を消す)

        fast.next が存在する間ループする:
          fast と slow を進める

        slow が削除対象の一つ前を指している
        slow.next に slow.next.next を入れる

        Time complexity: O(N)
        Space complexity: O(N)
        """

        fast, slow = head, head
        if not head:
            return head

        for _ in range(n):
            if not fast:
                raise Exception()
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            if not slow:
                raise Exception()

            fast, slow = fast.next, slow.next

        if not slow or not slow.next:
            raise Exception()

        slow.next = slow.next.next

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
