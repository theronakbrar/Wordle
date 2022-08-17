import random

f = open("words.txt", "r")
allWords = f.read().splitlines()
f.close()
word = str(allWords[random.randrange(5756)])
word.lower()
attempts = 7
win = False
usedUpLetters = []
misplacedLetters = []
correctLetters = []
lettersLeft = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("\n\n\n")
print("Welcome to Wordle. Try to correct the correct word within 6 turns.\n\
'-' means the letter is in the wrong position,\n '/' means the letter is\
correct but in the wrong spot,\n and '#' menas the letter is correct and in the right spot.\
\n")
print("_____")
while attempts > 0 and not(win):
    returnString = ""
    pWord = str(input("\nInsert Guess: "))[:5]
    pWord.lower()
    while allWords.count(pWord) == 0:
        pWord = str(input("That is not an acceptable word. Insert Guess: "))[:5]
    pWord.lower()
    if pWord == word:
        win = True
    for x,y in zip(pWord, word):
        if x == y :
            returnString += "#"
            if correctLetters.count(x) == 0:
                correctLetters.append(x)
        elif word.count(x) > 0:
            returnString += "/"
            if misplacedLetters.count(x) == 0:
                misplacedLetters.append(x)
        else:
            returnString += "-"
        if usedUpLetters.count(x) == 0:
            usedUpLetters.append(x)
    usedUpLetters.sort()
    misplacedLetters.sort()
    correctLetters.sort()
    lettersLeft = list(set(lettersLeft) - set(usedUpLetters) - set(misplacedLetters) - set(correctLetters))
    usedUpLetters = list(set(usedUpLetters) - set(misplacedLetters) - set(correctLetters))
    misplacedLetters = list(set(misplacedLetters) - set(correctLetters))
    correctLetters = list(set(correctLetters))
    lettersLeft.sort()
    usedUpLetters.sort()
    misplacedLetters.sort()
    correctLetters.sort()
    print(returnString +"\nTry Again")
    print("Here are the letters left: ")
    print(lettersLeft)
    print("Here are the used up Letters: ") 
    print(usedUpLetters)
    print("Here are the misplaced Letters: ") 
    print(misplacedLetters)
    print("Here are the correct Letters: ") 
    print(correctLetters)
    attempts-=1
if win:
    print(word)
    print("You win with " + str(attempts) + " attempts left!")
else:
    print("The word was: "+ word)
    print("You lose :/ Maybe try more next time.")