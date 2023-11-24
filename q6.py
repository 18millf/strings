word1: str = input("Word 1: ")
word2: str = input("Word 2: ")

shortest: int = min(len(word1), len(word2))

substr: str = ""

for i in range(shortest):
    substr = word1[-i:]
    if (substr == word2[:i]):
        break

print(substr)