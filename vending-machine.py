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


        

def vending_process(balence, confirm, cost, item_cost, paid, cost_check, change_check, check, cost_of_item, items, list, item_count, correct_amount, start_system_check):
    if start_system_check == False:
        def coinsystem(balence): # Balence checker 
            balence = input("Enter coins: (EG. 1.00 = £1) ") # Asks user to input their money
            try:
                balence = float(balence)
            except:
                print("Please only enter a nuber such as 0.5 or 1.00")
                coinsystem(balence)
            return balence

        def itemselection(confirm, cost, item_cost, check, cost_of_item, items):
            while confirm == False: # While items have not been confirmed run script below
                itemchoice = input("Enter '000' to confirm item slection - Please enter item ID: ") # Asking for item ID's or 000 to confirm the order/items chosen
                try:
                    itemchoice = int(itemchoice)
                except:
                    print("Please enter a ID 1-14. ")
                    itemselection(confirm, cost, item_cost, check, cost_of_item, items)

                if itemchoice == 000: # If the user enters 000 it kicks the user out of the while loop
                    confirm = True # Set's confirm to True so it stops asking them to enter items/confirm items

                elif itemchoice >= 1 and itemchoice <= 14: # If the item chosen is within the range of item ID's continue.
                    itemchoice = itemchoice - 1 # Changes the ID to match list syntax [0] = 1st position in the list.
                    cost_of_item = itemslistcost[itemchoice] # Check the itemslistcost for the cost by using the itemchoice as the number variable as the user inputed this earlier, Then save this to cost of item
                    print("Selected item: ",  itemlist[itemchoice], f"for £{cost_of_item:.2f} ") # Tells the user what item they added and the cost to 2 decimal places
                    check = int(input(f"Input the number {itemchoice + 1} again to confirm adding this item to your purchase " ))# Asks the user to enter the ID again to confirm
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
                    itemselection(confirm, cost, item_cost, check, cost_of_item, items) # Makes the section of code that was defined re-run to mimic a loop.
    
            return cost 


        def checkchange(cost, balence, paid, cost_check, change_check, correct_amount):

            balence = balence - cost # Calculates the remaning balence which may be negative
            balence = round(balence, 2) # Fixes any python math bugs


            if balence < 0: # If the balence is negative
                balence = abs(balence) # Make it posotive 
                print(f"More money is needed to cover cost of items, please enter £{balence:.2f}") # Prints how much more money is needed to cover the ammout.
                extramoney = float(input("Enter coins: (EG. 1.00 = £1) ")) # Asks for their input of more coins


                while correct_amount == False: # Runs straight after, as already false.
                    if extramoney <= balence: # If balence is bigger than extra money entered run this:
                        extramoney = float(input(f"{extramoney} returned, please re-enter the more or the correct amount of money. ")) # Asks for more money and returns the old ammount.
                        if extramoney >= balence: # If extramoney is bigger than balence
                            correct_amount = True # Set correct ammount to true to escape the while loop.

                        else:
                            correct_amount = False # Any errors on checking leave it as false.

                    else:
                        correct_amount = True # If enough money was entered it proceeds and exits while loop.


                balence = extramoney - balence # New balence is showing minusing the money entered from the old balence.
                balence = round(balence, 2) # Rounded to fix python maths.

            if balence == 0: # If balence is 0
                print("No more money is needed.") # Prints the fact that no more money is needed to be entered or returned.

            else: # If it's not 0
                print("We owe you some change!") # Prints the fact we owe the user change.
                cost_check = False # Set's cost check to false as it was true before.


            while cost_check == False: # Starts while loop
                for coin in posotive_coins: # For the amount of coins in the coins we have run this loop.
                    if balence <= 0: # If balence is bigger than 0 
                        cost_check = True # Cost check is true, escaping the loop.

                    elif balence >= coin: # Else balence is bigger than the coins we have
                        print(f"£{coin:.2f} Returned") # Return the biggest coin first
                        balence = balence - coin # Takeaway the coin from the amount left
                        balence = round(balence, 1) # Round it to fix python maths.
                


        # Where code actually starts running ---------------------------------------------------

        print(" Cereal Bar = 1 \n Doritos = 2 \n Squares = 3 \n Ruffles = 4 \n Walkers = 5 \n Freddo = 6 \n Twix = 7 \n Bounty = 8 \n Chocolate Bar = 9 \n Bottled Water = 10 \n Fanta = 11 \n Coke = 12 \n Haribo = 13 \n Moam = 14") # Prints itemlist to the user each item on a new line.
        balence = coinsystem(balence) # Calls the coin system function and takes balence as a returned value.
        cost = itemselection(confirm, cost, item_cost, check, cost_of_item, items) # Calls item selection and holds coin as a returned value.
        checkchange(cost, balence, paid, cost_check, change_check, correct_amount) # Runs costcheck function with parsed variables.
        print("Any remaning change has been returned if coins allow.") # Prints this message to show sometimes we cannot return all the change.
        print(f"Now pushing items: ") # Shows message after items have been paid for. 
        start_system_check = False # Set's system check to false if it was not already to ensure it does not re-run.


        # Returns what items they choose, and then + 1 moves to next items ---------
        for x in range(len(items)): # For number in range of the length of the list called items
            print(items[item_count]) # Print the number of items in place item
            item_count = item_count + 1 # Then item count = itemcounts + 1




# Runs first before actual script to turn on/off machine ---------------------------
while start_system_check == True: # While true, run this code loop.
    startsystem = input("Welcome Customer, please press 1 to procced to purchase or 2 to shutdown machine. ") # Asks for the user input to run or shutdown.
    try: 
        startsystem = int(startsystem) # Trys to convert to a interger
    except:
        print("Please only enter 1 or 2") # If not it runs this and shows error message
        notint = True # Ensures the error does not flag 2x
        start_system_check = True # Re-starts the loop for the user


    if startsystem == 1: 
        start_system_check = False # If they enter 1, leave the while loop.
        vending_process(balence, confirm, cost, item_cost, paid, cost_check, change_check, check, cost_of_item, items, list, item_count, correct_amount, start_system_check) # Runs the main code function with all parsed variables.

    elif startsystem == 2:
        print("Shutting down vending machine.") # If user enters 2, the system is exited.
        sys.exit() # System Exit

    else:
        if notint == False: # Ensures it has not already failed once.
            print("Please enter 1 or 0.") # Shows error message if not.

            
