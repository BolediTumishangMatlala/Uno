#import the random class
import random

#create an uno deck
deck = []

#create list of card colours
card_colour = ["Green", "Yellow", "Blue", "Red"]

#create a list of card numbers
card_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#join colour and the card number
for colour in card_colour:
    # Add the "0" card once
    deck.append({"colour": colour, "number": "0"})
    # Add numbers 1-9 twice
    for number in range(1, 10):
        deck.append({"colour": colour, "number": str(number)})
        deck.append({"colour": colour, "number": str(number)})


#create a list of card actions
card_action = ["skip", "Reverse", "Draw 2"]

#join colour and action cards
for colour in card_colour:
    for action in card_action:

        # Add each action card twice for each color
        deck.append({"colour": colour, "action": action})
        deck.append({"colour": colour, "action": action})

#create a list of wild cards
wild_cards=["Wild", "Wild Draw Four"]

#join colour and wild cards
#for colour in card_colour:
for wild in wild_cards:
    
    deck.append({ "wild type": wild})
    deck.append({ "wild type": wild})
    deck.append({ "wild type": wild})
    deck.append({ "wild type": wild})



#display the deck in order
print(deck)

#shuffle the deck
random.shuffle(deck)

print("......................")
#display the shuffled deck
print(deck)
print(len(deck))

print("Welcome to the UNO card game! ENJOY!!")
print("How many players are going to play?  Choose between 2 and 10")
#Repeat until the input is true
while True:
 #initiallize the number of players with the user's inout 
    no_of_players = input()
#check if the input can be converted into an integer
    if no_of_players.isdigit():
        no_of_players = int(no_of_players)
    #Check if the number is between 2 and 10
        if 2<= no_of_players <=10:
         print(f" {no_of_players} players are going to play.")
         break
        else:
         print("Please enter a number between 2 and 10.")
    else:
        print("Please enter a number between 2 and 10.")

#ask for players names
player_names=[]
for player in range(no_of_players):
   player_name=input(f"Enter the name of player {player + 1}: ")
   #add players name to the list of players
   player_names.append(player_name)

#display the list of players
print("Players' names are:", player_names)

# Sort the player names alphabetically
player_names.sort()

#display the player list in alphabetical order          #this is going to be the order of the game
print("Players' order:", player_names)