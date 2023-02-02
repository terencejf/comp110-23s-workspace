"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730491324"

word = input("Enter a 5-character word: ")
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
character = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + character + " in " + word)

counter = 0

if word[0]== character:
    print(character + " found at index 0")
    counter += 1
if word[1]== character:
    print(character + " found at index 1")
    counter += 1
if word[2]== character:
    print(character + " found at index 2")
    counter += 1
if word[3]== character:
    print(character + " found at index 3")
    counter += 1
if word[4]== character:
    print(character + " found at index 4")
    counter += 1

if counter == 0:
    print("No instances of " + character + " in " + word)

if counter == 1:
    print("1 instance of " + character + " in " + word)

if counter > 1:
    print(str(counter) + " instances of " + character + " in " + word)