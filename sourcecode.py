#!/usr/bin/env python
# coding: utf-8

# This project is my version of the popular hangman game. 
# 
# The following modules are used here:
# 
# 1. The random module is used to pickout random words from the preset list.
# 2. The string module is used to handle strings and use string functions as per requirement.
# 
# The following variable are used here:
# 
# 1. item -> is a list holding words.
# 2. start -> is an integer that controls the repeatibility of the game.
# 3. correct -> Keeps track of the correct words.
# 4. wrong -> keeps track of the wrong words.
# 5. random_item -> is the random word chosen.
# 6. length_item -> is the length of the random word.
# 7. word -> holds the blank spaces of the word.
# 8. word_list -> is a list that dynamically updates as the user guesses.
# 9. guess -> string variable that takes user input for the letter.
# 10. score -> holds the total score earned by the user. 
# 

# In[1]:


#Modules and initialization
import random
import string
item=['computer','mouse','keyboard','monitor','printer','speaker','pendrive']
print("Welcome to typebamboo - A computer based hangman game\n")
print("Instructions:\n")
print("1. The words are computer input/output devices")
print("2. +5 and -1 for every correct and wrong guess respectively")
score=0
start=int(input("type 1 to play 0 to exit "))


# In[2]:


#Functional program
while(start==1):
    correct=0
    wrong=0
    random_item=random.choice(item)
    length_item=len(random_item)
    word="_"*length_item
    word_list=[]
    for i in range(length_item):
        word_list.append(word[i])
    print(word_list)
    print("start guessing!\n")
    while(correct<length_item):    
        guess=str(input("Guess:"))
        if(guess in random_item):
            index=random_item.index(guess)
            print("Correct")
            correct=correct+1
            word_list[index]=guess
            print(word_list)
        else:
            print("incorrect")
            wrong=wrong+1
    print("you have guessed the word!\n")
    print(random_item)
    score=score+((correct*5)-(wrong))
    print("your score is: ",score)
    start=int(input("type 1 to play again or 0 to exit"))

