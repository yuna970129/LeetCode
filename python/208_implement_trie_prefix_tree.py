class Node:
    def __init__(self):
        self.children = [None]*(ord('z')-ord('a')+1)
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        new_root = self.root
        for w in word:
            if new_root.children[ord(w)-ord('a')] == None:
                new_root.children[ord(w)-ord('a')] = Node()
            new_root = new_root.children[ord(w)-ord('a')]
        new_root.is_end = True

    def search(self, word: str) -> bool:
        new_root = self.root
        for w in word:
            if new_root.children[ord(w)-ord('a')] != None:
                new_root = new_root.children[ord(w)-ord('a')]
            else:
                return False
        if new_root.is_end == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        new_root = self.root
        for w in prefix:
            if new_root.children[ord(w)-ord('a')] != None:
                new_root = new_root.children[ord(w)-ord('a')]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
