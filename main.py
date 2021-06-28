from math import log, trunc
import random
from hangman_words import word_list
from hangman_art import stages,logo


print(logo)
chosen_word = random.choice(word_list)
print(f'your currently chosen word is {chosen_word}')

c_word = [] 
for i in range(len(chosen_word)):
    c_word+=chosen_word[i]


display = [] 
for i in range(len(chosen_word)):
    display+="_"
print(display)

lives = 6                                            
while display!=c_word and lives>0:
    guess = input('Guessa letter:  ').lower()
    flag = False 
    if guess in display:
        print(f'you\'ve already guessed {guess}')
        continue
    for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            display[i]=guess
            flag = True
            print(display)
            # for i in range(len(display)):
            #     print(f'{display[i]} ')        
    #made the wrong guess
    if flag==False:
        lives = lives -1 
        lives_remaining = 6 - lives
        print(f'you guessed the letter {guess}, that\'s not in the word. You lose a life!')
        print(stages[lives])

if lives == 0:
    print('fk ya loser')
else:
    print('you win champ!')        
