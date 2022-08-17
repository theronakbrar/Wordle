f = open("words.txt", "r")
allWords = f.read().splitlines()
allWords.sort()
f.close()
tries = 6
Notwords = []
words = []
while tries > 0:
    guess = str(input("Enter guess:"))[:5]
    corrections = str(input("Enter the status of each letter:\n '#' is correct, '/' is misplaced, '_' is wrong:\n"))[:5]
    for each in allWords:
        match = True
        for j in range(0,5):
            if(corrections[j] == "#" and each[j] != guess[j]):
                match = False
                break
            elif(corrections[j] == "/" and (each.count(guess[j]) == 0 or each[j] == guess[j])):
                match = False
                break
            elif(corrections[j] == "-" and each[j] == guess[j]):
                match = False
                break

        if not(match):
            Notwords.append(each)
        else:
            words.append(each)
    words.sort()
    words = list(set(words) - set(Notwords))
    for each in words:
        print(each)
    tries -= 1