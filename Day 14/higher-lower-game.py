from art import logo,vs
from game_data import data
import random
from replit import clear

# format them into the required format
def formatted_item(item):
  return  item['name'] +", " +item['description']+ " from "+ item['country']+"."


# print logo to screen
print(logo)
game_should_continue = True
score =0
 # generate a  random dictionary from list
question_A = random.choice(data)
    # print(question_A)
question_B = random.choice(data)
while game_should_continue :
   
    print(question_A)
    print(question_B)
    if question_A == question_B :
      question_B = random.choice(data)
    
    print(f"Compare A:{formatted_item(question_A)}")
    print(vs)
    print(f"Against B: {formatted_item(question_B)}")
    
    
    # store user input in a variable
    choice = input("Who has more followers? Type 'A' or 'B':\n")
    
    # compare user input follower count 
    follower_count_A = question_A['follower_count']
    follower_count_B = question_B['follower_count']
    if choice =="A" and follower_count_A > follower_count_B:
      score += 1
      question_A = question_B
      clear()
      print(f"You're right! Current score: {score}.")
    elif choice =="B" and follower_count_A < follower_count_B :
      score +=1
      question_B = question_A
 
      
      # question_A = random.choice(data)
      # formatted_A = question_A['name'] +", " +question_A['description']+ " from "+ question_B['country'] + "."
      clear()
      print(f"You're right! Current score: {score}.")
    
    
    else:
      game_should_continue = False
      clear()
      print(f"Sorry, that's wrong. Final score:{score}")
    
  
# preserve the not chosen question as A and choose second random question
# If wrong game ends

# repeat game if correct answer is guessed


  