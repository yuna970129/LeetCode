# The code becomes inefficient because it repeatedly checks the occurrence of all characters through 
# the "is_repeating_letter" function to verify if it's a repeating substring.
# This redundant calculation occurs every iteration over the string,
# which diminishes the efficiency of the code.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The length of the longest substring consisting of only one character,
        # with at most k different characters, in a given string
        
        def is_repeating_letter(char, chars, _k):
            max_val = max(chars.values())
            repeating_letters = set([k for k, v in chars.items() if v == max_val])
            if char not in repeating_letters:
                return False
            if sum(chars.values()) - chars[char] > _k:
                return False
            return True

        start, end = 0, 0
        l = 0
        chars = defaultdict(int)
        _k = 0

        while end < len(s):
            chars[s[end]] += 1
            if not is_repeating_letter(s[end], chars, _k):
                _k += 1
            while _k > k and start <= end:
                chars[s[start]] -= 1
                if not is_repeating_letter(s[start], chars, _k):
                    _k -= 1
                start += 1

            l = max(l, end - start + 1)
            end += 1

        return l
