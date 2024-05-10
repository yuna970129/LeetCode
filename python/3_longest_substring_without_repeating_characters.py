# The existing algorithm involves reconstructing the dictionary within the loop,
# leading to a worst-case time complexity of O(n^2).

# By using the sliding window approach, with start and end pointers,
# you can traverse the string while updating start to resolve character conflicts,
# thus maintaining a valid substring.
# This allows the problem to be solved with a single traversal of the string,
# reducing the time complexity to O(n).
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        letters = {}
        max_len = 0

        i = 0
        while i < len(s):
            if s[i] not in letters:
                letters[s[i]] = i
            else:
                max_len = max(len(letters), max_len)
                i = letters[s[i]] + 1
                letters = {}
                letters[s[i]] = i
            i += 1
        
        return max(max_len, len(letters))
