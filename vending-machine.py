cost = 0
balence = 0
change = 0
combinedbal = 0
confirm = False
itemcost = 0
paid = False
costcheck = False
changecheck = True
check = 0
costofitem = 0

list = ""
# Change names away as the = will not work.
CEREALBAR = 0.5
DORITOS = 1.2
SQUARES = 1.0
RUFFLES = 1.2
WALKERS = 0.6
FREDDO = 9.90
TWIXBAR = 1.0
BOUNTYBAR = 0.9
CHOCOLATEBAR = 0.8
BOTTLEDWATER = 0.9
FANTA = 1.5
COKE = 1.6
HARIBO = 1.3
MOAM = 0.9



itemlist = ["Cereal Bar", "Doritos", "Squares", "Ruffles", "Walkers", "Freddo", "Twix", "Bounty", "Chocolate Bar", "Bottled Water", "Fanta", "Coke", "Haribo", "Moam"]
itemslistcost = [0.5, 1.2, 1.0, 1.2, 0.6, 9.99, 1.0, 0.9, 0.8, 0.9, 1.5, 1.6, 1.3, 0.9]


items = []
def vending_process(balence, confirm, cost, itemcost, paid, costcheck, changecheck, check, costofitem, items, list):

    def coinsystem(balence):
        balence = float(input("Enter coins: (EG. 1.00 = £1) "))
        return balence

    def itemselection(confirm, cost, itemcost, check, costofitem, items):
        while confirm == False:
            itemchoice = int(input("Enter '000' to confirm item slection - Please enter item ID: "))


            if itemchoice == 000:
                confirm = True

            elif itemchoice >= 1 and itemchoice <= 14:
                costofitem = itemslistcost[itemchoice]
                print("Selected item: ",  itemlist[itemchoice], f"for £{costofitem:.2f} ")
                check = int(input(f"Input the number {itemchoice} again to confirm adding this item to your purchase " ))

                if check != itemchoice:
                    print("Item not added. ")

                else:
                    itemchoice = itemchoice - 1
                    itemcost = itemslistcost[itemchoice]
                    cost = cost + itemcost
                    items.append(itemlist[itemchoice])

            else:
                print("Please enter a valid ID code for an item.")
                itemselection(confirm, cost, itemcost)

        return cost 


    def checkchange(cost, balence, paid, costcheck, changecheck):

        balence = balence - cost
        balence = round(balence, 2)


        if balence < 0:
            balence = abs(balence)
            print(f"More money is needed to cover cost of items, please enter {balence}")
            extramoney = float(input("Enter coins: (EG. 1.00 = £1) "))
            changecheck = True
            balence = extramoney - balence
            balence = round(balence, 2)
        else:
            print("We owe you some change!")
            costcheck = False


        while costcheck == False:
            if balence >= 1:
                balence = balence - 1
                balence = round(balence, 1)
                print("£1 Returned")
            elif balence >= 0.5:
                balence = balence - 0.5
                balence = round(balence, 1)
                print("50P Returned")
            elif balence >= 0.2:
                balence = balence - 0.2
                balence = round(balence, 1)
                print("20P Returned")
            elif balence >= 0.1:
                balence = balence - 0.1
                balence = round(balence, 1)
                print("10P Returned")
            elif balence <= -1 and changecheck == False:
                balence = balence + 1
                balence = round(balence, 1)
                print("£1 Returned")
            elif balence >= -0.5 and changecheck == False:
                balence = balence + 0.5
                balence = round(balence, 1)
                print("50P Returned")
            elif balence >= -0.2 and changecheck == False:
                balence = balence + 0.2
                balence = round(balence, 1)
                print("20P Returned")
            elif balence >= -0.1 and changecheck == False:
                balence = balence + 0.1
                balence = round(balence, 1)
                print("10P Returned")
            elif balence == 0:
                costcheck = True



    print(" Cereal Bar = 1 \n Doritos = 2 \n Squares = 3 \n Ruffles = 4 \n Walkers = 5 \n Freddo = 6 \n Twix = 7 \n Bounty = 8 \n Chocolate Bar = 9 \n Bottled Water = 10 \n Fanta = 11 \n Coke = 12 \n Haribo = 13 \n Moam = 14")
    balence = coinsystem(balence)
    cost = itemselection(confirm, cost, itemcost, check, costofitem, items)
    checkchange(cost, balence, paid, costcheck, changecheck)
    print("Change has been returned")
    print(f"Now pushing - ")
    print(items)


vending_process(balence, confirm, cost, itemcost, paid, costcheck, changecheck, check, costofitem, items, list)


