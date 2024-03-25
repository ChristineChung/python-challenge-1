#CC's Petite Boucherie - Interactive Menu

#Empty List to store customer order

[
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]
    
#Sub Menu for customer's choosing
# Menu dictionary

menu = {
    "Appetizer": {
        "Burrata": 15.50,
        "Waffle Fries": 5.00,
        "Pita and Hummus": 12.90,
        "Pear Salad": 18.75
    },
    "Main": {
        "Branzino": 45.00,
        "Chicken Milanese": 30.00,
        "Kale Caesar Salad": 18.00,
        "Short Ribs": 32.00,
        "Steak": {
            "Au Poivoire": 35.00,
            "NY Strip": 40.00,
            "Cajun Rib Eye": 55.00
        },
        "Pasta": {
            "A La Vongole": 18.00,
            "Homemade Lasagna": 24.00
        }
    },
    "Drinks": {
        "Wine": {
            "Red": 12.00,
            "White": 14.00,
            "Rose": 16.00
        },
        "Cocktail": {
            "Martini": 21.00,
            "Old Fashioned": 22.00,
            "French 75": 24.00
        },
        "Soft Drinks": {
            "Kombucha": 4.00,
            "Iced Tea": 5.00,
            "Fresh OJ": 6.49
        }
    },
    "Dessert": {
        "Chocolate Mousse": 15.00,
        "Pies": {
            "Apple Crumble": 8.99,
            "Boston Creme": 9.49
        },
        "Coffee Gelato": 8.00,
        "Caramel Churros": 12.00,
        "Fresh Fruits": 6.00
    }
}
# Launch the store and present a greeting to the customer

print("Welcome to the CC's Petite Boucherie")

menu_dashes = "-" * 47

# Display the heading for the sub-menu
print(menu_dashes)
print(f"Today's menu")
print("Which section would you like to view? ")

# Create a variable for the menu item number
i = 1

# Create a dictionary to store the menu for later retrieval 
menu_items = {}

# Print the options to choose from menu headings (all the first level 
# dictionary items in menu).
for key in menu.keys():
        print(f"{i}: {key}")

# Store the menu category associated with its menu item number
        menu_items[i] = key

# Add 1 to the menu item number
        i += 1

 # Ask the customer which menu category they want to view

while True:

    # Get the customer's input
    menu_selection = input("Enter menu section number: ")

    # Exit the loop if user typed 'q'
    if menu_selection == 'q':
        break

 # Check if the customer's input is a number
    elif menu_selection.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():
            # Save the menu selection name to a variable
            menu_selection_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            print(f"You selected {menu_selection_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_selection_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Initialize a menu item counter
            item_counter = 1

            menu_items = {}

            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_selection_name].items():

                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2:.2f}")
                        menu_items[item_counter] = {
                            'name': key2,
                            'price': value2
                        }
                        # Add 1 to the item_counter
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value:.2f}")
                    menu_items[item_counter] = {
                            'name': key,
                            'price': value
                        }
                    # Add 1 to the item_counter
                    item_counter += 1
            
            print(menu_dashes)

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    break       

# Customer to place the order
place_order = True

# List to menu selection
menu_selection = []

# While we are still shopping...
while place_order:

    menu_choice = input("What would you like to order? ")

    # Get index of the order from the selected number
    choice_index = int(menu_choice) 

    quantity_choice = input("How many would you like? ")

    menu_selection.append(
        {

    "Item name": menu_items[choice_index]['name'], 
    "Price": menu_items[choice_index]['price'],
    "Quantity": int(quantity_choice)

        }
    )

    # Add order to the order list by finding the matching index and adding one to its value
    # menu_selection[choice_index] += 1

    print("-" * 50)

    # Inform the customer of the order purchase
    print("Great! We'll have that " + menu_items[choice_index]['name'] 
          + " order right out for you.")
    
   # menu_selection.append 

    # Provide exit option
    while True:
		# Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # Check the customer's input
        match keep_ordering.lower():
            # Customer chose yes
            case 'y':
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
            # Customer chose no
            case 'n':
                # Complete the order
                place_order = False
                # Since the customer decided to stop ordering, thank them for their order
                print("Thank you for your order.")
                # Exit the keep ordering question loop
                break
            # Customer typed an invalid input
            case _:
                # Tell the customer to try again
                print("I didn't understand your response. Please try again.")

# Once the order list is complete
print("-" * 50)

# Count instances of each order
print("You purchased: ")
print("Item name                | Price  | Quantity")
print("-------------------------|--------|----------")
for selection in menu_selection:
   
 # Gather the count of each order in the order list and print them alongside the orders
    
    item_name_spaces_count = 24 - len(selection['Item name']) - 1
    item_name_spaces = " " * item_name_spaces_count
    if selection['Price'] >= 10.0:
        price_spaces_count = 0
    else:
        price_spaces_count = 1
    price_spaces = " " * price_spaces_count
    print(f"{selection['Item name']}${item_name_spaces} | " +
          f"${selection['Price']:.2f}{price_spaces} | {selection['Quantity']}")
  
 # Calculate and display the total sum of the order
total_price = sum(item['Price'] * item['Quantity'] for item in menu_selection)
print("-" * 46)
print(f"Total: ${total_price:.2f}")