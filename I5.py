## Chinmay D. 10/27/2022 Hg5590
import random
def TreasureChest(a):
# Naming and starting the chest function
    x = []
    for i in range(a):
        x.append(random.randint(1,100))
    return x
def LootStash(a):
    y = []
    for i in range(a):
        y.append(random.randint(1,100))
    return y
# Creates and sets the bank function 
def Wager(b):
    z = int(input("Place a wager: "))
    while z>b:
        print("Insufficient funds")
# Asks the user for a wager input and accepts it in the 'lottery draw'

def Spin(z,y):
    spining = random.randint(0,1)
    if spining == 0:
        y-=z
        print("You Lost! '-_-'")
        print("Total Coins: "+str(y))
    else:
        y+=z
        print("You Won! '^_^'")
        print("Total Coins: "+str(y))
# Creates a function for a lottery drawing system which spins 
# the roullete wheel then determines whether or not you won
def Grab(z,y):
    spining=random.randint(0,1)
    if spining==0:
        y -= z
        print("You Lost! '-_-'")
        print("Total Coins: "+str(y))
    else:
        y+=z
        print("You Won! '^_^'")
        print("Total Coins: "+str(y))
# Creates a function for a lottery drawing system which grabs
# the result of the Treasure chest then determines whether or not you won
def Pirate():
# Creates main function
    print("PIRATE: game of chance")
    print("Total Coins: 100")
    y = 100
    x = TreasureChest(10)
    y = LootStash(10)
    while (len(y)>0):
        c = int(input('''How to play Pirate:
        Type "1" to spin the wheel and Type "2" to grab the chest: '''))
        if c==1:
            z= Wager(y)
            y = Spin(z,y)
        elif c ==2:
            z = Wager(y)
            y = Grab(z,y)
        else:
            print('''Type "1" to spin the wheel
            Type "2" to grab the chest:''')
    print("Your ran out of coins '0--O'")
# Explains the rules and then allows user to enter input and wager to continue the game
# till user is completely out of coins
Pirate()
# End of the function and fullfills all the criteria 