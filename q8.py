word1: str = input("Word 1: ")
word2: str = input("Word 2: ")

sequence1: str = "".join(sorted(word1))
sequence2: str = "".join(sorted(word2))

if sequence1 == sequence2:
    print("AMBIGRAM")
else:
    print("NOT AN AMBIGRAM")