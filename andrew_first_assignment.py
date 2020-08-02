"""
Hey Andrew! This is the assignment my friend Jake gave me. He already gave some sick feedback for it.
So whenever you finish, I'll send along my code and his notes. I'm not sure of the best way to organize
our code on here yet, so I may end up switching some stuff around if we end up with a lot of files.


ASSIGNMENT 1 -- INTRO
````````````````````````````````````````````````````````````````````````````````````````
1. Print out a greeting to the user
2. Make a function that adds two variables together and prints the output
3. Break a given string into a character array, then print the letters in alphabetical order with no duplicates.
   In python, an 'array' is generally a list.
"""

####################################
######### ANDREW'S CODE ############
####################################

name = input("Hello User, what is your name? ")
print("Welcome", name)

def assignment():
   dna = "tcgcgatcgc"
   dna2 = "tggggcatgc"

   recombination = dna + dna2
   lst = list(recombination)
   print(lst)

assignment()