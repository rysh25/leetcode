from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        list1、list2 どちらからも始められるように、ダミーノードを用意する
        curr にダミーノードを入れる

        list1 と list2 が存在する間ループする:
            list1.val < list2.val:
                curr の next を list1 にして、list1 を進める
            そうでなければ、curr の next を list2 にして、list2 を進める
            curr を進める

        ダミーの next を返す

        Time complexity: O(N)
        Space complexity: O(1)

        #LinkedList
        """

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next


sol = Solution()

n3 = ListNode(4, None)
n2 = ListNode(2, n3)
list1 = ListNode(1, n2)
n3 = ListNode(4, None)
n2 = ListNode(3, n3)
list2 = ListNode(1, n2)

ret = sol.mergeTwoLists(list1, list2)

curr = ret
while curr:
    print(curr.val)
    curr = curr.next
