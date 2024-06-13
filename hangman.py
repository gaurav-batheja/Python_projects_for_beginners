someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

import random
someWords = someWords.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
word = random.choice(someWords) 
tries=len(word)+2

print('Guess the word! HINT: word is a name of a fruit')
for i in word: 
     # For printing the empty spaces for letters of the word 
    print('_', end=' ') 
print()

guess_list=[]

while tries>0:
    guess = input("Enter a letter to guess- ")
    if not guess.isalpha() or len(guess)>1:
        print("Enter a valid input")
        continue
    
    if guess in word:
        if guess not in guess_list:
            guess_list.append(guess)
        if len(guess_list)==len(word):
            print("you got it right!!, the word was", word)
            e=input("press any key")
            break
        for i in word:
            if i in guess_list:
                print(i, end=' ')
            else:
                print("_", end=" ")
        print()
        print("you got that right, Tries left - ",tries)
    else:
        tries-=1
        for i in word:
            if i in guess_list:
                print(i, end=' ')
            else:
                print("_", end=" ")
        print()
        print("wrong!, Tries left - ", tries)
if tries==0:
    print("Sorry you lost, the word was",word)
    e=input("press any key")