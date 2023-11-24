master: str = input("Master Word: ")
test: str = input("Test word: ")

while len(test) > len(master):
    test = input("Test word too long, enter a shorter one: ")

print(f"{test} is{' not ' if test not in master else ' '}in {master}.");