class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        self.words = dictionary

    def search(self, searchWord):
        for word in self.words:
            # Length must match
            if len(word) != len(searchWord):
                continue

            # Count differences
            diff = 0
            for c1, c2 in zip(word, searchWord):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break

            # Exactly one character should differ
            if diff == 1:
                return True

        return False