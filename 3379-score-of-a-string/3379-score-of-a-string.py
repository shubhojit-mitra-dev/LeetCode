class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for index in range(1, len(s)):
            score += abs(ord(s[index - 1]) - ord(s[index]))
        return score
        