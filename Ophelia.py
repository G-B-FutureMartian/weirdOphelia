# this program brings all of the files for the Ophelia chatbot together
############################################################################
# This section deals with importing.
from random import choice
import sys

# This section deals with Ophelia's information
class O:
    

f.open("infoUsers.txt","r")
usr_name = f.read(11)
name = "Ophelia"
greetings = [
    "Hello. My name is Ophelia.",
    "Hi, I'm " + name + ".",
   # "Hello,  " + usr_name + ". My name is Ophelia."
    ]
responses = [
    "Hello"
    "Hi"
    ]
print("Gathered Info.")

usr_name = input("What is your name? ")

# file editing in this section.
f = open("infoUsers.txt", "w+")
str(usr_name)
f.write("USR_NAME = {0}".format(usr_name))
f.close()

print(choice(greetings))
in1 = input()
