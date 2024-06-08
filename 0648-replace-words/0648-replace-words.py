class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = set(dictionary)
        def findRoot(word: str):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root:
                    return prefix
            return word
        words = sentence.split()
        return ' '.join([findRoot(word) for word in words])