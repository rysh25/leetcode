from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


def print_linked_list(name: str, head: Optional[ListNode]):
    print(f"{name}:")
    if not head:
        print()
        return
    curr = head
    while curr:
        print(curr.val, end=', ')
        curr = curr.next
    print()


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        Step 1. 真ん中を見つける
        slow ポインター、fast ポインターを用意して head を入れる
        slow を1づつ、fast を2づつ進めて、fast の next、next.next が存在するかぎり続ける
        slow が真ん中を見る様になる （例えばリストのサイズが5・6なら slow は3番目まで進む)

        Step 2. 後半を逆順にする
        slow.next に None を入れる (slow を前半の最後にする)
        curr に slow.next をいれる (これから slow の次を法はんの逆順の最後にする)
        prev に None を入れる
        curr が存在するかぎりループする:
            curr を tmp に退避させる
            curr を進める
            tmp.next に prev を入れる
            prev に tmp を入れる

        prev に真ん中までの逆順が入る

        Step 3. マージする
        head1 に head、had2 に prev を入れる
        head2 が存在するかぎりループする:
            head1.next を tmp に退避させる
            head1.next を head2 にする
            head1 に head2 を入れる
            head2 に tmp を入れる

        Time complexity: O(N)
        Space complexity: O(1)
        """

        if not head:
            return head

        # Step 1. Find middle
        slow, fast = head, head

        while fast.next and fast.next.next:
            if not slow:
                Exception()
            slow = slow.next
            fast = fast.next.next

        # Step 2. Reverse second half
        if not slow:
            Exception()
            return
        curr, prev = slow.next, None
        slow.next = None

        # print_linked_list("head", head)

        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp

        # print_linked_list("prev", prev)

        # Step 3. Merge two lists
        head1, head2 = head, prev
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp


sol = Solution()

n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
list1 = ListNode(1, n2)

print_linked_list("input", list1)

sol.reorderList(list1)

print_linked_list("result", list1)
