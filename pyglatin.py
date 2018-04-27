
for i in range(100):
    print("Enter a word to translate")
    word = input()
    word = word.lower()
    firstLetter = word[0]
    print(word[1:] + word[0] + "ay")
