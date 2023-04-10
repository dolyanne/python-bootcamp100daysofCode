# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1 + name2
name_to_lower_case = names.lower()
t = name_to_lower_case.count("t")
r = name_to_lower_case.count("r")
u = name_to_lower_case.count("u")
e = name_to_lower_case.count("e")
l = name_to_lower_case.count("l")
o = name_to_lower_case.count("o")
v = name_to_lower_case.count("v")
e = name_to_lower_case.count("e")
true = t+r+u+e
# print(true)
love = l+o+v+e
# print(love)
true_love = int(str(true)+ str(love))
# print(true_love)
if (true_love) <10 or (true_love) > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love )> 40 and (true_love )< 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")
