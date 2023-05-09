from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        curr に head を入れる
        prev に None を入れる
        curr が存在する間ループする:
            curr を tmp に退避させる
            curr を進める
            tmp.next に prev を入れる
            prev に curr を入れる

            これにより、今回処理したノードが一つ前を見る様になる

        prev を返す

        Time complexity: O(N)
        Space complexity: O(1)

        #LinkedList
        """

        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = None
        while curr:
            # print(curr.val)
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp

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
