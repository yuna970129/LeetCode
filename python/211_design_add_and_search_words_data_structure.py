from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.words = set()
        self.dot_words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)):
            self.dot_words.add(word[:i] + "." + word[i + 1 :])

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        elif word in self.dot_words:
            return True
        
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if word.replace(".", ch, 1) in self.dot_words:
                return True
 
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
