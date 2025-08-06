#the user plays a guessing game with the computer. 
# computer generates random integers between 1 and 10 using the random module. 
import random
comp_choice = random.randint(1,10)
# The user is prompted to guess the number
# The user inputs their guess, which is then compared to the computer's choice.
# If the user's guess matches the computer's choice, it is a tie.
# If the user's guess does not match, the computer wins.
while True:
  print("I'm thinking of a number between 1 and 10. Guess which one?") 
  user_choice = int(input("Your Guess:")) 
  if user_choice == comp_choice: 
    print("IT's A TIE") 
  else: print("YOU LOOSE, COMPUTER WINS!") 
