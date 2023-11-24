word: str = input()
(first, last) = (word[0], word[-1])

if first == last:
    print("The first and last letters are the same");
else:
    print("The first and last letters are different");