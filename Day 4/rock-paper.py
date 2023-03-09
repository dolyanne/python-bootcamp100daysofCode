# ## Rock Paper Scissors

# # Instructions

# Make a rock, paper, scissors game. 

# Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console. 

# Start the game by asking the player:

# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

# From there you will need to figure out: 
# * How you will store the user's input.
# * How you will generate a random choice for the computer.
# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
# * And also how you will give feedback to the player.


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Playing Rock Paper Scissors can be as simple as scissors cuts paper, paper covers rock, and rocks crushes scissors,
#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_input = random.randint(0,2)
print(f"computer chose {computer_input}")
if user_input == 0 and computer_input ==0 :
  print("You drew")
elif user_input ==0 and computer_input ==1:
  print("oops sorry you lost")
elif user_input ==0 and computer_input ==2:
  print("congratulations you won")
elif user_input ==1 and computer_input ==0:
  print("congratulations you won")
elif user_input ==1 and computer_input ==1:
  print("You drew")
elif user_input ==1 and computer_input ==2:
  print("oops sorry you lost")
elif user_input ==2 and computer_input ==0:
  print("oops sorry you lost")
elif user_input ==2 and computer_input ==1:
  print("congratulations you won")
elif user_input ==2 and computer_input ==2:
  print("You drew")

else:
  print("Type a number to play")




# TODO :add images to code