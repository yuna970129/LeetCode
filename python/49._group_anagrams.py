class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            letter_dict = [0]*26
            for i in list(word):
                letter_dict[ord(i)-97] += 1
            word_dict[tuple(letter_dict)].append(word)
        return word_dict.values()
