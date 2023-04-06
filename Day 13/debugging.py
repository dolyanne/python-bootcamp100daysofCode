############DEBUGGING#####################

#  step 1 Describe Problem
# function is suppose to run a for loop from 1 to 20 and if the iteration
#  reaches 20 print to the console, but the print never happens because i never get to 20

# def my_function():
  
#   for i in range(1, 21):# to fix this, range has an upper bound less the number so i only goes up to 19
#     if i == 20:# changing upper bound to 21 fixes the bug
#       print("You got it")
# my_function()

# step 2 Reproduce or replicate  the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # out of range error is thrown because unlike range, randint includes the values at both ends
# print(dice_imgs[dice_num])# hence when dice_num ==6 index 6 is out of range in dice imgs list changing range from(1,6) to (0,5) fixes the bug

#step 3 Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1995:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# else:
#   print("You are neither a millenial or a Gen Z")

# Fix the Errors
# age = int(input("How old are you?")) # type cast to get integer values
# if age > 18:
#     print(f"You can drive at age {age}.") #indentation issues with print f string to print age as numbber

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page =int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# print(word_per_page)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])