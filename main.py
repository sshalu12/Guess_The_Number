  
from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def printt(guess):
  if guess!=1: 
    print("Guess again.")
  else:
    print("You've run out of guesses, you lose.")

def Guess(guess):
  while guess>0 :
    print(f"You have {guess} attempts remaining to guess the number. ")
    no1=int(input("Make a guess: "))
    if no1>no :
      print("Too high")
      printt(guess)
      guess -=1
    elif no>no1 :
      print("Too low")
      printt(guess)
      guess -= 1
    elif no==no1 :
      print(f"You got it! The number was {no}. ")
      break
    
 
no=random.randint(1,100)
print(f"number {no} ")
if difficulty=="easy":
  Guess(10)
elif difficulty=="hard":
  Guess(5)
else:
  print("choose the valid difficulty level")




