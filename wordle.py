"""
This is wordle.
"""
import random

wordsList = ["guess", "guest", "tiger", "aloft", "plain", "plane", "human", "robot", "squat", "squad", "swift", "flare",
             "flame", "stage", "angle", "short", "hands", "rocks", "shirt", "belts", "apple", "adorn", "adore", "cramp",
             "abode", "delhi", "india", "music", "sound", "audio", "songs", "maker", "brick", "crane", "steep", "crack",
             "rings", "bells", "books", "study", "photo", "print", "organ", "fresh", "drive", "drink", "sleep", "break",
             "speed", "start", "obese", "daddy", "spice", "pouch", "punch", "cable", "balls", "socks", "shoes", "towel",
             "lover", "cards", "reads", "write", "right", "doubt", "charm", "chase", "chose", "mouse", "doors", "wheel",
             "abyss", "light", "match", "plays", "nails", ]
randomWord = random.choice(wordsList)
guesses = 0


def matchWord(word):
    global guesses
    wordUsed = word.lower()
    correct = {letter for letter, correct in zip(wordUsed, randomWord) if letter == correct}
    misplaced = set(wordUsed).intersection(set(randomWord)) - correct
    wrong = set(wordUsed) - set(randomWord)
    guesses += 1
    guessText = f'''Guess {guesses}: {f'You Lost. Word: {randomWord}' if guesses == 7 and len(correct) < 5 else ('You Win.' if guesses <= 7 and len(correct) == 5 else f'Correct: {correct}, Misplaced: {misplaced}, Wrong: {wrong}')}'''
    return guessText


while True:
    word = input("Guess The Word: ")
    wordGuessed = matchWord(word)
    print(wordGuessed)
    if guesses > 7 and 'You Lost.' in wordGuessed or (guesses <= 7 and 'You Win' in wordGuessed):
        break
