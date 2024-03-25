#My Own Solution ~ Due to time constraint and working hours
from classes import drink, vendingmachine

drinks = drink.drinks_selection()

run = int(input("Run Vending Machine (1 ~ run | 0 ~ stop) ? "))

while run == 1:
 

    print("Selections\n")
    
    i = 1
    
    for d in drinks:
        print(i, d[0], "RM",d[1])
        i+=1

    choice = int(input("\nSelect a drink you want to purchase: "))


    if choice == 1:
        print("\n\nCost for drink (RM): ", drinks[0][1])
        amount = float(input("Insert amount: $ "))
        balance = vendingmachine.calculation(drinks[0][1], amount)

        if balance < 0 :
            print("Please pay up RM ", abs(float(balance)))
            balance = abs(float(balance))
            top_up = float(input("Insert amount: "))
            balance -= top_up 
        print("Changes (RM)", balance)
        

    elif choice == 2:
        print("\n\nCost for drink (RM): ", drinks[1][1])
        amount = float(input("Insert amount: $ "))
        balance = vendingmachine.calculation(drinks[0][1], amount)

        if balance < 0 :
            print("Please pay up RM ", abs(float(balance)))
            balance = abs(float(balance))
            top_up = float(input("Insert amount: "))
            balance -= top_up 
        print("Changes (RM)", balance)
        

    elif choice == 3:
        print("\n\nCost for drink (RM): ", drinks[2][1])
        amount = float(input("Insert amount: $ "))
        balance = vendingmachine.calculation(drinks[0][1], amount)

        if balance < 0 :
            print("Please pay up RM ", abs(float(balance)))
            balance = abs(float(balance))
            top_up = float(input("Insert amount: "))
            balance -= top_up 
        print("Changes (RM)", balance)
        

    print("\n")

    run = int(input("Run Vending Machine (1 | 0) ? "))



#ChatGpt's answer
# class Drink:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class VendingMachine:
#     def __init__(self, drinks):
#         self.drinks = drinks
#         self.notes = [100, 50, 20, 10, 5]  # Available notes
#         self.notes_count = {note: 10 for note in self.notes}  # Initial note count in the machine

#     def display_menu(self):
#         print("Welcome to the Drink Vending Machine!")
#         print("Menu:")
#         for i, drink in enumerate(self.drinks, 1):
#             print(f"{i}. {drink.name} - ${drink.price}")

#     def buy_drink(self, choice, amount):
#         choice -= 1
#         if 0 <= choice < len(self.drinks):
#             selected_drink = self.drinks[choice]
#             if amount < selected_drink.price:
#                 print("Insufficient amount. Please insert more money.")
#                 return
#             change_due = amount - selected_drink.price
#             if change_due > 0:
#                 print(f"Your change: ${change_due}")
#                 self.return_change(change_due)
#             print(f"Enjoy your {selected_drink.name}!")
#         else:
#             print("Invalid selection. Please try again.")

#     def return_change(self, amount):
#         remaining_amount = amount
#         for note in self.notes:
#             while remaining_amount >= note and self.notes_count[note] > 0:
#                 print(f"Returning ${note}")
#                 remaining_amount -= note
#                 self.notes_count[note] -= 1

# # Sample drinks in the vending machine
# drinks = [Drink("Cola", 1.5), Drink("Water", 1.0), Drink("Juice", 2.0)]

# # Initialize vending machine
# vending_machine = VendingMachine(drinks)

# # Display menu
# vending_machine.display_menu()

# # Simulate a customer buying a drink
# choice = int(input("Enter the number of the drink you want to buy: "))
# amount = float(input("Insert amount: $"))

# # Process purchase
# vending_machine.buy_drink(choice, amount)