#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
	 
#Write the rest of your code below this line 👇

#choice  = input("Heads or Tails ? ")


generate_random = random.randint(0,1)


if generate_random == 1:
    print("Heads")
else :
    print ("Tails")


