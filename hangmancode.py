import random
import wordlist

#word_list= ["ardvark","baboon","camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("How to play")
print("-----------")
print("Guess any letter at first.")
print("If the letter is in the word, you'll be provided with the number of letters in the word with blanks.")
print("The letter you guessed will be entered into the blank if it is correct.")
print("If the letter is not in the word, you'll lose a life.\nIf you run out of lives, you lose the game.\nIf you manage to guess all letters of the word, you win.")
print("\nGOOD LUCK!")
lives=7

chosen_word= random.choice(wordlist.word_list)
#print(chosen_word)

display=[]
for i in range(len(chosen_word)):
    display.append("_")
#print(f"{' '.join(display)}\n")

end_of_game=False
while end_of_game==False and lives!=0:
    found=False
    guess= input("\nGuess a letter: ")
    guess= guess.lower()
    
    if guess in display:
        print("You already guessed this letter!")
    
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            found=True
            display[position]=guess
            
    print(f"{' '.join(display)}\n")
    
    if "_" not in display:
        end_of_game=True
        print("\nYOU WON :)")
        
    if found==False:
        lives-=1
        print(stages[lives])
        print(f"You have {lives} lives left")

if lives==0:
    print("\nYOU LOST!!")