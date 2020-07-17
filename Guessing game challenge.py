# Guessing game challenge.


import random as rdm
from random import randint

num1 = rdm.randint(1,100)


# Welcome message for players 

welcome = """
 
 Welcome to Guessing Game Challenge
     
      ***MAKE YOUR GUESS***
      #####################
             #Rules#
             
    1. The no. is b/w 1-100
    2. The no. is an integer
    3. 'Warmer!'= you are close
    4. 'Colder!'= not close enough
    
        SO, ARE YOU READY ?
             
            **BEGIN**

"""
print(welcome)

# empty list for tracking all consecutive guesses made by players.

guess_list = [0]

# asks input form players and compare with system generated random integer

while True:
    
    ans = int(input("Enter any no. make a guess!: "))
    
    pass

    if (ans < 1) or (ans > 100):
        print("Out of bounds!")
        
        break
    
    elif ans == num1:
        print("Hurrah you won!!!")
        print("Total no. of guesses made: {}".format(guess_list))
        
        break
        
        
    elif ans != num1 and abs(ans-num1) <= 10:
        print("Warmer!")
        guess_list.append(ans)
        
    else:
        print("Colder!")
        guess_list.append(ans)
        
        continue

