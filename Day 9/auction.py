from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
auction_dict ={}
def start_auction ():
  name =input("Please type your name \n")
  bid = int(input("How much do you want to bid? \n"))
  auction_dict[name]=bid
  print(auction_dict)
  more_bidders = input("Are there other bidders? type yes if there are and No if there are no bidders").lower()

  if more_bidders =="yes":
    clear()
    start_auction()
  else:
    for bidder in auction_dict :
      winner = auction_dict[bidder]
      if auction_dict[bidder] > winner:
       new_winner = auction_dict[bidder]
       print(f"The new winner is {bidder} and the bid was {new_winner}")

start_auction()

  
     
   
  

  