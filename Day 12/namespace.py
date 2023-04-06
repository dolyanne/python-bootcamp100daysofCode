#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
attempts =10

  

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def play_game():
  is_game_over =False
  while not is_game_over:
      level = input("choose the difficulty lever, h for hard and e for easy. 10 guesses in easy mode, only 5 guesses in hard mode: \n")
      user_input = float(input("Type a number between 1 and 100:\n"))
      if level == "h":
        attempts =5
      computer_pick = random.randint(1,100)
      if user_input == computer_pick :
        is_game_over =True
        print(f"you guess right the number is {computer_pick} and you guessed {user_input}" )
      else:
         print(f"oops is try again you have {attempts -1} guesses left  you guessed {user_input}" )
         return attempts - 1

      
        
      
    
  
       



  
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



while attempts > 0 :
  play_game()