# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# Empty List to store customer order
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to CC's Food Truck")

menu_dashes = "-" * 47

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print(menu_dashes)
    print("From which menu would you like to order? ")

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

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + " - " + key2)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_selection = input("Enter menu section number or 'q' to quit: ")

            # Exit the loop if user typed 'q'
            if menu_selection.lower() == 'q':
                break

            # 3. Check if the customer typed a number
            elif menu_selection.isdigit():

                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in range(1, i):

                    # Store the item name as a variable
                    menu_selection_name = list(menu_items[menu_selection].values())[0]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {menu_selection_name} would you like? (Default: 1) ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "name": menu_selection_name,
                        "price": menu_items[menu_selection]["Price"],
                        "quantity": quantity
                    })

                else:
                    # Tell the customer that their input isn't valid
                    print("Invalid menu selection. Please try again.")

            else:
                # Tell the customer they didn't select a menu option
                print("Invalid input. Please try again.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    if order_list:
        print("\n--- Your Order ---")
        total_price = sum(item['price'] * item.get('quantity', 1) for item in order_list)

        for index, item in enumerate(order_list, start=1):
            quantity = item.get('quantity', 1)
            subtotal = quantity * item['price']
            print(f"{index}: {item['name']} x{quantity} - ${subtotal:.2f}")

        print(f"Total: ${total_price:.2f}")
        print(menu_dashes)
    else:
        print("\nNo items were ordered.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
        
        #Check customer input
        match keep_ordering:
            case 'y':      
                break
            case 'n':
                place_order = False
                break
            case _:
                print("Invalid input. Please try again.")


# Complete the order
# Since the customer decided to stop ordering, thank them for their order
print("Thank you for your order!")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order_list:
    # 7. Store the dictionary items as variables
    item_name = item['name']
    item_price = item['price']
    item_quantity = item.get('quantity', 1)

    # 8. Calculate the number of spaces for formatted printing
    name_spaces = 26 - len(item_name)
    price_spaces = 6 - len(str(item_price))

    # 9. Create space strings
    name_space_str = " " * name_spaces
    price_space_str = " " * price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_space_str}| ${item_price:.2f}{price_space_str}| {item_quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices
total_cost = sum(item['price'] * item.get('quantity', 1) for item in order_list)

print(f"\nTotal cost: ${total_cost:.2f}")