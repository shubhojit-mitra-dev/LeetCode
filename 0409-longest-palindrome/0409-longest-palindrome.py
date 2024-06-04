class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1: return 1
        char_set = set()
        length = 0
        for char in s:
            if char in char_set:
                char_set.remove(char)
                length += 2
            else:
                char_set.add(char)
        if char_set:
            length += 1
        
        return length
