from typing import Dict, Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional["Node"]) -> "Optional[Node]":
        """
        1度目のループで、ノードと値をコピーしながら、コピー元と、コピー先の対応付け行う辞書を作る。
        2度目のループで、コピー元の、next と random をキーに、対応付辞書から、コピー先のノードを取得し、
        設定する。
        コピー先のヘッダーを返す。

        ※ __hash__() メソッド、__eq__() メソッドを定義していない独自にクラスも、辞書のキーに設定できるのか？
          おそらく、Python が id() 関数の値を元に、ハッシュキーを生成しているのだろう。
          C++ で、unordered_map のキーにポインターを利用できるのと同じか。

        - Time complexity: O(N)
        - Space complexity: O(N)

        #LinkedList
        """
        oldToCopy: Dict["Node", "Node"] = {}
        if not head:
            return None

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            if curr.next:
                copy.next = oldToCopy[curr.next]
            if curr.random:
                copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head] if head else None
