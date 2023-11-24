word: str = input("Word: ")

if word == word[::-1]:
    print("PALINDROME!")
else:
    print("NOT A PALINDROME :(")