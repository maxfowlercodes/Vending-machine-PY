import sys


cost = 0
balence = 0
change = 0
combined_balence = 0
confirm = False
item_cost = 0
paid = False
cost_check = True
change_check = True
check = 0
cost_of_item = 0
item_count = 0
correct_amount = False
start_system_check = True

itemlist = ["Cereal Bar", "Doritos", "Squares", "Ruffles", "Walkers", "Freddo", "Twix", "Bounty", "Chocolate Bar", "Bottled Water", "Fanta", "Coke", "Haribo", "Moam"] # Sets the name of items
itemslistcost = [0.5, 1.2, 1.0, 1.2, 0.6, 9.90, 1.0, 0.9, 0.8, 0.9, 1.5, 1.6, 1.3, 0.9] # Sets the price of each item. [0] = 0.5 = Cereal Bar  - Change numbers here to update prices
items = [] # Holds selected items
coins = [1, 0.5, 0.2, 0.1, -0.1, -0.2, -0.5, -1]
posotive_coins = [1, 0.5, 0.2, 0.1]


        

def vending_process(balence, confirm, cost, item_cost, paid, cost_check, change_check, check, cost_of_item, items, list, item_count, correct_amount):

    def coinsystem(balence): # Balence checker 
        balence = float(input("Enter coins: (EG. 1.00 = £1) ")) # Asks user to input their money
        return balence

    def itemselection(confirm, cost, item_cost, check, cost_of_item, items):
        while confirm == False: # While items have not been confirmed run script below
            itemchoice = int(input("Enter '000' to confirm item slection - Please enter item ID: ")) # Asking for item ID's or 000 to confirm the order/items chosen


            if itemchoice == 000: # If the user enters 000 it kicks the user out of the while loop
                confirm = True # Set's confirm to True so it stops asking them to enter items/confirm items

            elif itemchoice >= 1 and itemchoice <= 13: # If the item chosen is within the range of item ID's continue.
                itemchoice = itemchoice - 1 # Changes the ID to match list syntax [0] = 1st position in the list.
                cost_of_item = itemslistcost[itemchoice] # Check the itemslistcost for the cost by using the itemchoice as the number variable as the user inputed this earlier, Then save this to cost of item
                print("Selected item: ",  itemlist[itemchoice], f"for £{cost_of_item:.2f} ") # Tells the user what item they added and the cost to 2 decimal places
                check = int(input(f"Input the number {itemchoice + 1} again to confirm adding this item to your purchase " )) # Asks the user to enter the ID again to confirm
                itemchoice = itemchoice + 1 # Resets the value to check the right value.

                if check != itemchoice: # If the answer is not ID then run this script
                    print("Item not added. ") # Does not add it to the cost/cancels the additon of this item.

                else:  # Anything else and this bit of script is run
                    itemchoice = itemchoice - 1 # Resets the value again to now print the correct price as list placment is different.
                    item_cost = itemslistcost[itemchoice] # Sets the cost of the single item by using the choice ID as the list locator. 
                    cost = cost + item_cost # Add the single item_cost to the overall cost of all items
                    items.append(itemlist[itemchoice]) # Adds the purchased item to the items[] list by using ID to locate the positon within the itemlist[]

            else: # If anything other than an ID is entered run this script
                print("Please enter a valid ID code for an item.") # Prints text in speech marks
                itemselection(confirm, cost, item_cost) # Makes the section of code that was defined re-run to mimic a loop.
 
        return cost 


    def checkchange(cost, balence, paid, cost_check, change_check, correct_amount):

        balence = balence - cost
        balence = round(balence, 2)


        if balence < 0:
            balence = abs(balence)
            print(f"More money is needed to cover cost of items, please enter {balence}")
            extramoney = float(input("Enter coins: (EG. 1.00 = £1) "))


            while correct_amount == False:
                if extramoney <= balence:
                    extramoney = float(input(f"{extramoney} returned, please re-enter the more or the correct amount of money. "))
                    if extramoney >= balence:
                        correct_amount = True

                    else:
                        correct_amount = True

                else:
                    correct_amount = True

            costcheck = False
            balence = extramoney - balence
            balence = round(balence, 2)

        if balence == 0:
            print("No more money is needed.")

        else:
            print("We owe you some change!")
            cost_check = False

    #for coin in coins:
        #if balence >= coin:


        while cost_check == False:
            for coin in posotive_coins:
                if balence <= 0:
                    cost_check = False

                elif balence >= coin:
                    print(f"{coin:.2f} Returned")
                    balence = balence - coin
                    balence = round(balence, 1)
            

            cost_check = True



    print(" Cereal Bar = 1 \n Doritos = 2 \n Squares = 3 \n Ruffles = 4 \n Walkers = 5 \n Freddo = 6 \n Twix = 7 \n Bounty = 8 \n Chocolate Bar = 9 \n Bottled Water = 10 \n Fanta = 11 \n Coke = 12 \n Haribo = 13 \n Moam = 14")
    balence = coinsystem(balence)
    cost = itemselection(confirm, cost, item_cost, check, cost_of_item, items)
    checkchange(cost, balence, paid, cost_check, change_check, correct_amount)
    print("Any remaning change has been returned if coins allow.")
    print(f"Now pushing items: ")
    start_system_check = False

    for x in range(len(items)):
        print(items[item_count])
        item_count = item_count + 1



while start_system_check == True:
    startsystem = int(input("Welcome Customer, please press 1 to procced to purchase or 2 to shutdown machine. "))

    if startsystem == 1:
        start_system_check = False
        vending_process(balence, confirm, cost, item_cost, paid, cost_check, change_check, check, cost_of_item, items, list, item_count, correct_amount)

    elif startsystem == 2:
        print("Shutting down vending machine.")
        sys.exit()

    else:
        print("Please enter 1 or 0.")
