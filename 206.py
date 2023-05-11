# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" | None = None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        curr に head を入れます。
        prev に None を入れます。
        curr が存在する間ループします。:
            curr を tmp に退避させます。
            curr を進める
            tmp.next に prev を入れます。
            prev に curr を入れます。

            これにより、今回処理したノードが一つ前を見る様になる

        prev を返します。

        Time complexity: O(N)
        Space complexity: O(1)

        #LinkedList

        Args:
            head (ListNode | None): 単方向連結リストのヘッドを指定します。

        Returns:
            ListNode | None: 指定された単方向連結リストを逆順にしたものを返します。
        """

        curr: ListNode | None = head
        prev: ListNode | None = None
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
