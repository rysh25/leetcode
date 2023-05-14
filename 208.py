class TrieNode:
    def __init__(self, val: str = "", is_end: bool = False):
        self.children: dict[str, TrieNode] = {}
        self.is_end = is_end


class Trie:
    """
    トライを表すクラスです。

    トライは、ツリー構造で、文字列の先頭部分(接頭辞: prefix)の共通部分を共有して保存することで、
    O(n) (n は文字列の長さ) での検索を可能にします。

    トライの木構造は、頂点を1つ持ちます。1つの文字が1つのノードに対応し、文字列の接頭辞が共通する場合
    ノードを共有することで無駄なくデータを持つことができます。

    #Tree
    #Trie
    """

    def __init__(self):
        """トライオブジェクトを初期化します。"""

        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """文字列をトライに挿入します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            word (str): 挿入する文字列を指定します。
        """

        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)

            curr = curr.children[c]

        curr.is_end = True

    def search(self, word: str) -> bool:
        """
        word がトライに存在するかどうかを調べます。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            word (str): 検索対象の文字列を指定します。

        Returns:
            bool: word がトライに存在した場合、True を返します。
            そうでなければ、False を返します。
        """

        curr = self.root
        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        以前に挿入された文字列に、prefix を接頭辞として持つ文字列があったかどうかを調べます。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            prefix (str): 検索対象の接頭辞

        Returns:
            bool: 前に挿入された文字列に、prefix を接頭辞として持つ文字列があった場合は True を返し、
            それ以外の場合は False を返します。
        """

        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
