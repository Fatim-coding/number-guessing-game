# import necessary moduels
import random
import time

# pick a number between 1 and 100
number=random.radint(1,100)

def intro():
    print("may I ask you for your name?")
# declaring name variable global so it can be accessed outside the function
global Name
name = input() #ask for the name
print(name +",we are going to play a game. I am thinking of a number between 1 and 100")
if(number%2==0):
    x='even'
else:
    x='odd'
print("\nThis is an {} number".format(x))
time.sleep(.5)
print("go ahead. guess!")

def pick():
    guessesThaken = 0

    #if the number of guesses is less than 6
    while guessesThaken <6:
        time.sleep(.25)
        #inserts the place to enter guess
        enter=input("guess: ")

        #check if a number was entered
try:

            #stores the guess as an integer instead of a string
            guess = int(enter)

if guess<=100 and guess>=1: #if they are in range
    guessesThaken=guessesThaken+1 #adds one guess time the player is wrong
    if guessesThaken<6:
      if guess<number:
        print("The guess of the number that you  have entered is too low")
    if guess>number:
         print("The guess of the number that you  have entered is too high")
    if guess != number:
        time.sleep(.5)
        print("Try Again!")

#if the guess is right, then we are going to jump out of the two while block
if guess==number:
     break


if guess>100 or guess<1:
    print("silly goose! That number isn't in the range!")
    time.sleep(.25)
print("Please enter a number between 1 and 100")

except: #if a number wasn't entered
print("I don't think that "+enter+" is a number. Sorry")
			
if guess == number:
		guessesTaken = str(guessesTaken)
		print('Good job, {}! You guessed my number in {} guesses!'.format(name, guessesTaken))

if guess != number:
  print('Nope. The number I was thinking of was ' + str(number))

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
	intro()
	pick()
	print("Do you want to play again?")
	playagain=input()
    