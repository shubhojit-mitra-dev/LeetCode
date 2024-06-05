
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = Counter(words[0])
        for i in words:
            result = result & Counter(i)
        return list(result.elements())
