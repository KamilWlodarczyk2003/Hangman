from itertools import count
import random
from Words import word_list
from art import stages, logo

chosen_word=word_list[random.randint(0,2)]
print(f"Testing mode: {chosen_word}")

print(logo)

display=[]
for x in chosen_word:
    display.append("_")

lives=6

end_of_the_game=False

while not end_of_the_game:

    guess=str(input("Guess the letter\n")).lower()

    error=0

    for x in range(0,len(chosen_word)):
        if chosen_word[x]==guess:
            display[x]=chosen_word[x]
        else:
            error+=1
    if error==len(chosen_word):
        lives-=1
    if lives==0 or display.count("_")==0:
        end_of_the_game=True

    print(stages[lives])
    print(display)