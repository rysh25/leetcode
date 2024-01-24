from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int | None = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def create_tree(list: list[int | None]):
    from collections import deque

    if not list:
        return

    root = TreeNode(list[0])
    parent = root
    q: deque[TreeNode] = deque()
    q.append(root)
    i = 1
    while len(q):
        parent = q.popleft()
        if i < len(list) and list[i] is not None:
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.append(node)
            parent.left = node
        i += 1
        if i < len(list) and list[i] is not None:
            node = TreeNode(list[i])
            # print(f"list[{i}]={list[i]}")
            q.append(node)
            parent.right = node
        i += 1

    return root


def print_tree(name: str, root: TreeNode | None):
    from collections import deque

    print(f"{name}: ", end="")

    if not root:
        print()
        return

    q: deque[TreeNode] = deque()
    q.append(root)
    # print(f"push: root={root.val}")

    while len(q):
        curr = q.popleft()
        print(curr.val, end=", ")

        if curr.left:
            # print(f"push: curr.left={curr.left.val}")
            q.append(curr.left)
        if curr.right:
            # print(f"push: curr.right={curr.right.val}")
            q.append(curr.right)

    print()
    
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode|None) -> int:
        """
        ノード値が 1 から 9 までの数字である二分木が与えられます。
        パス内のノード値の少なくとも 1 つの順列が回文である場合、二分木内のパスは擬似回文であると言われます。

        ルート ノードからリーフ ノードに向かう擬似回文パスの数を返します。
        
        
        DFS を行い、リーフについた際に、パス内のノード数が奇数の場合で、ノードの値の頻度が奇数のものが1つであるか、
        パス内のノード数が偶数の場合で、ノードの値の頻度が奇数のものが1つもない場合、
        擬似回文とみなし、ans をインクリメントする。
        
        - Time complexity: O(n)
        - Space complexity: O(h)
        
        #DFS
        #BinaryTree

        Args:
            root (TreeNode | None): ノード値が 1 から 9 までの数字である二分木

        Returns:
            int: ルート ノードからリーフ ノードに向かう擬似回文パスの数を返します。
        """
        
        self.ans = 0
        
        def dfs(node: TreeNode, freq: list[int]):
            if node.val is not None:
                freq[node.val] += 1
            # print(f"node.val={node.val}, freq={freq}")
            
            if node.left is None and node.right is None:
                # print(f"node.left is None and node.right is None")
                # print(f"node.val={node.val}, freq={freq}")
                even_count = 0
                odd_count = 0
                freq_sum = 0
                
                for i in range(len(freq)):
                    freq_sum += freq[i]
                    if freq[i] == 0:
                        pass
                    elif freq[i] % 2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1
                        
                # print(f"even_count={even_count}, odd_count={odd_count}")
                        
                if freq_sum % 2 == 1 and odd_count == 1:
                    # print(f"even_count={even_count}, odd_count={odd_count}")
                    # print(f"node.val={node.val}, freq={freq}")
                    self.ans += 1
                elif freq_sum % 2 == 0 and odd_count == 0:
                    # print(f"even_count={even_count}, odd_count={odd_count}")
                    # print(f"node.val={node.val}, freq={freq}")
                    self.ans += 1
            
            if node.left is not None:
                dfs(node.left, freq)
            
            if node.right is not None:
                dfs(node.right, freq)
            
            if node.val is not None:
                freq[node.val] -= 1
                
        freq: list[int] = [0] * 10
        
        if root is None or root.val is None:
            return 0
        
        dfs(root, freq)
        
        return self.ans
        
sol = Solution()
print(sol.pseudoPalindromicPaths(root = create_tree([2,3,1,3,1,None,1])))
print(sol.pseudoPalindromicPaths(root = create_tree([2,1,1,1,3,None,None,None,None,None,1])))
print(sol.pseudoPalindromicPaths(root = create_tree([9])))
print(sol.pseudoPalindromicPaths(root = create_tree([9,5,4,5,None,2,6,2,5,None,8,3,9,2,3,1,1,None,4,5,4,2,2,6,4,None,None,1,7,None,5,4,7,None,None,7,None,1,5,6,1,None,None,None,None,9,2,None,9,7,2,1,None,None,None,6,None,None,None,None,None,None,None,None,None,5,None,None,3,None,None,None,8,None,1,None,None,8,None,None,None,None,2,None,8,7]))) # 1
