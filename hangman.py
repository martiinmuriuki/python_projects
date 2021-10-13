import random
from word import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has gussed..

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('you have', lives,'lives left, You have used these letters: ', ' '.join(used_letters))

        # what current word is(ie w-rd)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
        
        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
             word_letters.remove(user_letter)
            else:
                lives = lives-1 # takes a life
                print("letter is not in the word.")
    
        elif user_letter in used_letters:
            print("you have already used that character. please try again")
    
        else:
            print('Invalid character. please try again')

    # gets here when len(word_letters) == 0  OR when lives == 0
    if lives == 0:
        print('you died, sorry. The word was ', word)
    else:
        print('You guessed the word ', word,'!!')

hangman()