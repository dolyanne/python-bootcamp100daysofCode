# file = open("Day 24/my.txt")
with open("Day 24/my.txt") as file:
    content = file.read()# read a file
    
    print(content)
 #file.close() # you need to close the file to free up space
    
with open("Day 24/my.txt", mode="a") as file:
   file.write("\nnew test again")
    
 